#!/usr/bin/env python3
"""ai-architecture-digest collector.

状態は SQLite（scripts/.cache/collect.db）の articles 台帳で一元管理する。
  status: fetched（取得済み・未生成） / generating（生成処理中） / generated（生成済み） / error

2 段構え（ローカル実行前提）:
  fetch    : sources.yml の各ソースから新着を取得 → articles に status='fetched' で登録（決定的・LLM不要）
  generate : status='fetched' の記事を `claude -p` に渡して事例MDを作る → src/content/cases/<id>.md、status='generated'
  status   : 台帳サマリ（status別・source別件数）を表示

無人ジョブ向けの分割生成（`claude -p` を使わない経路）:
  generate-emit  : fetched を claim（generating へ）し、生成プロンプトを JSONL で出力（LLMは呼ばない）
  generate-ingest: tmux セッション内の Claude が生成した JSON を取り込み → write_case → generated
  ※ claude-job（tmux・-p非使用）で回すときは generate ではなく emit→(セッション生成)→ingest を使う。
    -p 経路（generate/run）はローカル手動実行用に残している。

取得方式:
  - rss                : RSS を parse（stdlib）→ 本文は bs4 抽出
  - sitemap / page-diff: ソース別 discovery（catalog ロジックを移植・自己完結）でURL列挙 → 各ページから title/date/text
  - manual             : 自動取得不可（robots.txt 等）。スキップ

設計:
  - 生成は claude CLI（サブスク認証・APIキー不要）。1記事=1呼び出し、ローカルでコスト管理。
  - 冪等: URL が台帳 or 既存 case md にあればスキップ。
  - 語彙は vocab/*.yml を prompt に渡して寄せる（無ければ新語可）。
使い方:
  python scripts/collect.py fetch [--source ID] [--max-new-per-source N] [--max-total N] [--max-fetch M] [--dry-run]
  python scripts/collect.py generate [--limit N] [--dry-run]
  python scripts/collect.py generate-emit [--limit N] [--out FILE]
  python scripts/collect.py generate-ingest [--input FILE]
  python scripts/collect.py retry [--limit N] [--include-generating]
  python scripts/collect.py status
  python scripts/collect.py run [--source ID] [--max-new-per-source N] [--max-total N] [--generate-limit N]
"""
from __future__ import annotations

import argparse
import gzip
import json
import re
import sqlite3
import subprocess
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
SOURCES_FILE = ROOT / "sources.yml"
VOCAB_DIR = ROOT / "vocab"
DB_PATH = SCRIPT_DIR / ".cache" / "collect.db"
CASES_DIR = ROOT / "src" / "content" / "cases"
UA = "Mozilla/5.0 (compatible; ai-architecture-digest/0.1)"

MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}
MONTHS.update({m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July", "August",
     "September", "October", "November", "December"], 1)})
MONTHS["Sept"] = 9
LOC_RE = re.compile(r"<loc>([^<]+)</loc>")
JSONLD_DATE_RE = re.compile(r'"datePublished"\s*:\s*"([^"]+)"')
# 3文字略称・フル月名・Sept を許容（"Jul 15, 2026" / "July 15, 2026" / "Sept 1, 2026"）
INTEXT_DATE_RE = re.compile(r"\b([A-Z][a-z]{2,8})\.?\s+(\d{1,2}),?\s+(20\d\d)\b")


def log(*a):
    print(*a, file=sys.stderr)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def slugify(s: str) -> str:
    out = re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
    return out or "item"


def fetch_bytes(url: str, timeout: float = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def load_sources() -> list[dict]:
    d = yaml.safe_load(SOURCES_FILE.read_text(encoding="utf-8")) or {}
    return d.get("sources", [])


# ================= SQLite 台帳 =================
def db_connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    con.execute(
        """CREATE TABLE IF NOT EXISTS articles(
            id TEXT PRIMARY KEY,
            url TEXT UNIQUE NOT NULL,
            source_id TEXT, source_name TEXT, tier TEXT,
            title TEXT, published TEXT, text TEXT, vendors TEXT,
            status TEXT NOT NULL DEFAULT 'fetched',
            case_path TEXT, fetched_at TEXT, generated_at TEXT, error TEXT,
            retry_count INTEGER NOT NULL DEFAULT 0,
            last_attempt_at TEXT)"""
    )
    columns = {r[1] for r in con.execute("PRAGMA table_info(articles)")}
    if "retry_count" not in columns:
        con.execute("ALTER TABLE articles ADD COLUMN retry_count INTEGER NOT NULL DEFAULT 0")
    if "last_attempt_at" not in columns:
        con.execute("ALTER TABLE articles ADD COLUMN last_attempt_at TEXT")
    con.execute("CREATE INDEX IF NOT EXISTS idx_status ON articles(status)")
    con.execute("CREATE INDEX IF NOT EXISTS idx_source ON articles(source_id)")
    sync_cases_to_db(con)
    con.commit()
    return con


def sync_cases_to_db(con: sqlite3.Connection) -> int:
    """既存Markdownを正として台帳のgenerated状態を補完・修復する。"""
    repaired = 0
    for p in CASES_DIR.glob("*.md"):
        txt = p.read_text(encoding="utf-8")
        m = re.search(r"^source_url:\s*(\S+)", txt, re.M)
        if not m:
            continue
        url = m.group(1).strip()
        case_path = str(p.relative_to(ROOT))
        row = con.execute("SELECT status,case_path FROM articles WHERE url=?", (url,)).fetchone()
        if row:
            if row["status"] != "generated" or row["case_path"] != case_path:
                con.execute(
                    """UPDATE articles
                       SET status='generated', case_path=?, generated_at=COALESCE(generated_at,?), error=NULL
                       WHERE url=?""",
                    (case_path, now_iso(), url),
                )
                repaired += 1
            continue
        con.execute(
            """INSERT OR IGNORE INTO articles(
                   id,url,source_id,status,case_path,generated_at
               ) VALUES(?,?,?,?,?,?)""",
            (p.stem, url, _fm_field(txt, "source_id"), "generated", case_path, now_iso()),
        )
        repaired += 1
    if repaired:
        log(f"ledger sync: {repaired} article(s) marked generated from Markdown")
    return repaired


def _fm_field(md: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(\S+)", md, re.M)
    return m.group(1).strip() if m else ""


def db_has_url(con, url: str) -> bool:
    return con.execute("SELECT 1 FROM articles WHERE url=?", (url,)).fetchone() is not None


def db_has_id(con, aid: str) -> bool:
    return con.execute("SELECT 1 FROM articles WHERE id=?", (aid,)).fetchone() is not None


def db_insert_fetched(con, s, title, url, date, text) -> bool:
    aid = f'{s["id"]}-{slugify(title)[:60]}'
    if db_has_url(con, url) or db_has_id(con, aid):
        return False
    con.execute(
        """INSERT INTO articles(id,url,source_id,source_name,tier,title,published,text,vendors,status,fetched_at)
           VALUES(?,?,?,?,?,?,?,?,?, 'fetched', ?)""",
        (aid, url, s["id"], s["name"], s.get("tier"), title, date, text,
         json.dumps(s.get("vendors", []), ensure_ascii=False), now_iso()),
    )
    con.commit()
    log("  +", aid)
    return True


def claim_fetched(con: sqlite3.Connection, limit: int) -> list[sqlite3.Row]:
    """生成対象を排他的にclaimし、別プロセスから見えないgeneratingへ移す。"""
    con.execute("BEGIN IMMEDIATE")
    sql = """SELECT * FROM articles
             WHERE status='fetched' AND text IS NOT NULL AND text!=''
             ORDER BY published DESC, fetched_at ASC"""
    params: tuple = ()
    if limit:
        sql += " LIMIT ?"
        params = (limit,)
    rows = con.execute(sql, params).fetchall()
    attempted_at = now_iso()
    for row in rows:
        con.execute(
            """UPDATE articles
               SET status='generating', retry_count=retry_count+1,
                   last_attempt_at=?, error=NULL
               WHERE id=? AND status='fetched'""",
            (attempted_at, row["id"]),
        )
    con.commit()
    return rows


# ================= RSS / Atom =================
def _ln(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def parse_feed(xml_bytes: bytes) -> list[dict]:
    root = ET.fromstring(xml_bytes)
    items: list[dict] = []
    for e in root.iter():
        if _ln(e.tag) not in ("item", "entry"):
            continue
        title, link, published = "", "", ""
        for child in e:
            ln = _ln(child.tag)
            if ln == "title" and not title:
                title = (child.text or "").strip()
            elif ln == "link":
                rel, href = child.get("rel"), child.get("href")
                if href and rel in (None, "alternate") and not link:
                    link = href
                elif (child.text or "").strip() and not link:
                    link = child.text.strip()
            elif ln in ("pubDate", "published", "updated", "date") and not published:
                published = (child.text or "").strip()
        items.append({"title": title, "link": link, "date": norm_date(published)})
    return items


def norm_date(s: str) -> str:
    if not s:
        return ""
    for fn in (
        lambda x: parsedate_to_datetime(x).date().isoformat(),
        lambda x: datetime.fromisoformat(x.replace("Z", "+00:00")).date().isoformat(),
        lambda x: datetime.strptime(x.strip(), "%b %d, %Y").date().isoformat(),
    ):
        try:
            return fn(s)
        except Exception:
            continue
    return ""


def _clean(el) -> str:
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True))


def extract_text(url: str, limit: int = 8000) -> str:
    return fetch_page(url)[2][:limit]


def fetch_page(url: str, timeout: float = 30) -> tuple[str, str, str]:
    """Fetch a page → (title, published_date, body_text)."""
    html = fetch_bytes(url, timeout).decode("utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")
    raw_title = soup.title.string if soup.title and soup.title.string else ""
    title = re.sub(r"\s*[|｜–—-]\s*[^|｜–—-]{1,40}$", "", raw_title).strip() if raw_title else ""
    title = re.sub(r"\s+", " ", title)
    for t in soup(["script", "style", "nav", "header", "footer", "aside", "form"]):
        t.decompose()
    main = soup.find("main") or soup.find("article") or soup.body or soup
    body = _clean(main)
    return title, parse_any_date(html, body), body[:8000]


def parse_any_date(html: str, text: str) -> str:
    m = JSONLD_DATE_RE.search(html)
    if m and norm_date(m.group(1)):
        return norm_date(m.group(1))
    m = INTEXT_DATE_RE.search(text)
    if m:
        mon, day, yr = m.groups()
        mo = MONTHS.get(mon) or MONTHS.get(mon[:3])
        if mo:
            try:
                return datetime(int(yr), mo, int(day)).date().isoformat()
            except Exception:
                pass
    return ""


# ================= non-RSS discovery（catalog ロジックを移植） =================
# discoverer は {"url":..(必須).., "title":..(任意).., "date":..(任意)..} の list を返す。
# title/date が取れないソースは fetch_page 側でページから補完する。newest-first で返すのが望ましい。
AZURE_LANDING = "https://learn.microsoft.com/en-us/azure/architecture/"
AWS_API = "https://aws.amazon.com/api/dirs/items/search"
AWS_DIRECTORY = "directory-migration-cards-interactive-alias-architecture-center"
NON_HTML_EXT = (".pdf", ".zip", ".docx", ".pptx", ".xlsx")
NON_ARTICLE_DOMAINS = {
    "youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be",
    "linkedin.com", "www.linkedin.com",
}


def is_non_article(url: str) -> bool:
    p = urllib.parse.urlsplit(url)
    return p.netloc.lower() in NON_ARTICLE_DOMAINS or p.path.lower().endswith(NON_HTML_EXT)


def discover_claude_blog() -> list[dict]:
    xml = fetch_bytes("https://claude.com/sitemap.xml").decode("utf-8", errors="ignore")
    out, seen = [], set()
    for loc in LOC_RE.findall(xml):
        loc = loc.strip()
        if loc.startswith("https://claude.com/blog/") and loc not in seen:
            seen.add(loc); out.append({"url": loc})
    return out


def discover_llamaindex_blog() -> list[dict]:
    html = fetch_bytes("https://www.llamaindex.ai/blog").decode("utf-8", errors="ignore")
    out, seen = [], set()
    for path in re.findall(r'href="(/blog/[^"#?]+)"', html):
        if path.rstrip("/") == "/blog":
            continue
        u = "https://www.llamaindex.ai" + path
        if u not in seen:
            seen.add(u); out.append({"url": u})
    return out


def discover_aws_architecture_center() -> list[dict]:
    # 内部API（非公開）。title/date/url を直接返す。新しい順（dateCreated desc）。
    params = {
        "item.directoryId": AWS_DIRECTORY, "item.locale": "en_US",
        "sort_by": "item.dateCreated", "sort_order": "desc", "size": "50",
    }
    req = urllib.request.Request(
        f"{AWS_API}?{urllib.parse.urlencode(params)}",
        headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    out = []
    for e in data.get("items", []):
        f = e.get("item", {}).get("additionalFields", {})
        title, link = f.get("title") or f.get("heading"), f.get("ctaLink")
        if not title or not link or is_non_article(link):
            continue
        raw = f.get("publishedDate") or f.get("date") or ""
        out.append({"url": link, "title": title, "date": raw[:10] if raw else ""})
    return out


def discover_azure_architecture_center() -> list[dict]:
    # learn.microsoft.com の azure_en-us_*.xml（7分割・plain XML・lastmod あり）→ /en-us/azure/architecture/。
    idx = fetch_bytes("https://learn.microsoft.com/_sitemaps/sitemapindex.xml").decode("utf-8", errors="ignore")
    sub_re = re.compile(r"^https://learn\.microsoft\.com/_sitemaps/azure_en-us_\d+\.xml$")
    subs = [l for l in LOC_RE.findall(idx) if sub_re.match(l)]
    dated, seen = [], set()
    fails = 0
    for sm in subs:
        try:
            xml = fetch_bytes(sm).decode("utf-8", errors="ignore")
        except Exception as e:
            fails += 1
            log("  fail-sitemap", sm, type(e).__name__)
            if fails >= 3:  # 500storm 等で連続失敗が続くなら打ち切り（fetch 全体の長時間化を防ぐ）
                log("  azure discovery: 連続失敗が多いため打ち切り"); break
            continue
        fails = 0
        for block in xml.split("<url>")[1:]:
            m = LOC_RE.search(block)
            if not m:
                continue
            loc = m.group(1).strip()
            if "/en-us/azure/architecture/" not in loc or loc == AZURE_LANDING or loc in seen:
                continue
            seen.add(loc)
            lm = re.search(r"<lastmod>([^<]*)</lastmod>", block)
            dated.append((lm.group(1) if lm else "", loc))
    dated.sort(key=lambda p: p[0], reverse=True)
    return [{"url": u, "date": norm_date(d)} for d, u in dated]


GCP_ARCH_HREF_RE = re.compile(
    r'''href=["'](?:https?://docs\.cloud\.google\.com)?(/architecture/[^"'#?]+)["']''')


def discover_gcp_architecture_center() -> list[dict]:
    # docs.cloud.google.com のサブサイトマップ（60分割）が恒常500のため、hub ページの HTML
    # から /architecture/ 記事リンクを採る。各 hub の共有左ナビに記事一覧(~390)が入っている。
    # landing は hub のみ／各 hub は全記事リンクを静的HTMLで返す。lastmod無し（日付はページから補完）。Issue #21。
    base = "https://docs.cloud.google.com"
    out, seen, hubs = [], set(), []

    def harvest(html: str) -> None:
        for href in GCP_ARCH_HREF_RE.findall(html):
            url = base + href.rstrip("/")
            if url not in seen:
                seen.add(url); out.append({"url": url})

    try:
        landing = fetch_bytes(base + "/architecture").decode("utf-8", errors="ignore")
        harvest(landing)  # landing 自身のリンクも採る（再fetchしない）
        hubs = sorted({h.rstrip("/") for h in GCP_ARCH_HREF_RE.findall(landing)
                       if h.rstrip("/").count("/") == 2})  # /architecture/<hub> のみ巡回
    except Exception as e:
        log("  gcp landing-fail", type(e).__name__)
    for path in hubs:
        if len(out) >= 200:  # 早期打ち切り（共有ナビは各 hub でほぼ同一・日付が無く順序も任意のため）
            break
        try:
            harvest(fetch_bytes(base + path).decode("utf-8", errors="ignore"))
        except Exception as e:
            log("  gcp page-fail", path, type(e).__name__)
    return out


DISCOVERERS = {
    "claude-blog": discover_claude_blog,
    "llamaindex-blog": discover_llamaindex_blog,
    "aws-architecture-center": discover_aws_architecture_center,
    "azure-architecture-center": discover_azure_architecture_center,
    "google-cloud-architecture-center": discover_gcp_architecture_center,
}


# ================= fetch =================
def _fetch_rss(con, s, args, remaining: int) -> int:
    try:
        feed = parse_feed(fetch_bytes(s["url"]))
    except Exception as e:
        log("skip", s["id"], type(e).__name__, e); return 0
    feed.sort(key=lambda x: x["date"], reverse=True)
    added = 0
    limit = min(args.max_new_per_source, remaining)
    for it in feed:
        if added >= limit:
            break
        if not it["link"] or not it["title"] or is_non_article(it["link"]) or db_has_url(con, it["link"]):
            continue
        if args.dry_run:
            log("  would add", it["title"][:60]); added += 1; continue
        try:
            text = extract_text(it["link"])
        except Exception as e:
            log("  text-fail", it["link"], type(e).__name__); text = ""
        if db_insert_fetched(con, s, it["title"], it["link"], it["date"], text):
            added += 1
    return added


def _fetch_nonrss(con, s, args, remaining: int) -> int:
    try:
        items = DISCOVERERS[s["id"]]()
    except Exception as e:
        log("skip", s["id"], type(e).__name__, e); return 0
    fetch_limit = min(args.max_fetch, args.max_new_per_source, remaining)
    fresh = [it for it in items if not db_has_url(con, it["url"]) and not is_non_article(it["url"])][:fetch_limit]
    log(f"  {s['id']}: {len(items)} urls found, fetching {len(fresh)} for content")
    got = []
    for it in fresh:
        try:
            ptitle, pdate, text = fetch_page(it["url"])
        except Exception as e:
            log("  page-fail", it["url"], type(e).__name__); continue
        title = it.get("title") or ptitle
        date = it.get("date") or pdate
        if title:
            got.append((title, it["url"], date, text))
    got.sort(key=lambda x: x[2] or "", reverse=True)
    added = 0
    for title, u, date, text in got[: min(args.max_new_per_source, remaining)]:
        if args.dry_run:
            log("  would add", title[:55], date); added += 1; continue
        if db_insert_fetched(con, s, title, u, date, text):
            added += 1
    return added


def cmd_fetch(args):
    con = db_connect()
    sel = [s for s in load_sources() if (not args.source or s["id"] == args.source)]
    added = 0
    for s in sel:
        remaining = args.max_total - added
        if remaining <= 0:
            break
        if s.get("method") == "rss":
            added += _fetch_rss(con, s, args, remaining)
        elif s["id"] in DISCOVERERS:
            added += _fetch_nonrss(con, s, args, remaining)
        elif args.source:
            log(f"  (no auto-fetch for method={s.get('method')}: {s['id']})")
    prefix = "would fetch" if args.dry_run else "fetch done"
    log(f"{prefix}: {added} new article(s)")


# ================= generate =================
def load_vocab() -> dict:
    v = {}
    for name in ["patterns", "cloud", "industries", "outcomes", "types"]:
        d = yaml.safe_load((VOCAB_DIR / f"{name}.yml").read_text(encoding="utf-8"))
        v[name] = list(d.values())[0]
    return v


def build_prompt(row, vocab: dict) -> str:
    return f"""あなたはAIアーキテクチャ事例カタログの編集者です。以下の記事から日本語の「事例カード」を1件作ります。
出力は **JSONオブジェクトのみ**（コードフェンス無し・前後に説明文を付けない）。

記事メタ:
- source_name: {row['source_name']}
- source_url: {row['url']}
- published_at: {row['published']}

記事本文（抜粋・整形済み）:
\"\"\"
{(row['text'] or '')[:7000]}
\"\"\"

次のキーを持つJSONを出力:
{{
  "type": "case|guidance|opinion|announcement",
  "ai_relevant": true または false（true=AIアーキ(LLM/ML/エージェント/RAG/ベクトル検索/モデル配信/AI基盤運用)が記事の構成の中心 / false=周辺技術が主題: 3Dグラフィックス・レイトレ/量子/汎用インフラ運用/カンファレンス報告など）,
  "title": "日本語の再構成タイトル（記事名の直訳でなく『何のシステム/話か』を一言で）",
  "title_original": "元記事タイトル（英語のまま）",
  "company": "実装主体の企業名。無ければ空文字",
  "industry": "industriesから1つ。該当なければ cross-industry",
  "cloud": ["cloudから該当するもの（複数可・無ければ空配列）"],
  "patterns": ["patternsから該当するもの1〜4個"],
  "components": ["記事に出てくる具体的なサービス/製品名（例: Amazon Bedrock, OpenSearch）。無ければ空配列"],
  "outcome": {{"type": "outcomesから1つ"}},
  "summary": "『## 概要』に入れる2〜3文の日本語要約",
  "design_point": ["『## 設計のポイント』の箇条書き。再利用できる設計判断を1項目ずつ、2〜4個（各項目1文程度・文字列の配列）"],
  "use_case": ["『## 使いどころ』の箇条書き。誰に/どんな場面で効くかを1項目ずつ、2〜4個（各項目1文程度・文字列の配列）"]
}}

判定の指針:
- type: 具体的な実装事例=case / 手引き・リファレンス=guidance / 意見・考察=opinion / 提供開始・機能告知=announcement
- 具体的な構成が読み取れない記事でも type で分類して出す（事例以外は company/components が空でよい）
- ai_relevant=false（非AI）のときは深掘りファセットを無理に埋めない: patterns / components は空配列、design_point / use_case は空配列でよい。
  ただし summary（概要）と company / industry / cloud / outcome は通常どおり埋める（網羅カバレッジ用の軽量カードになる）。

語彙（できるだけこの中から選ぶ。適切な語が無ければ新しい語を作ってよい）:
- types: {vocab['types']}
- industries: {vocab['industries']}
- cloud: {vocab['cloud']}
- outcomes: {vocab['outcomes']}
- patterns: {vocab['patterns']}
"""


def run_claude(prompt: str, timeout: float = 180) -> str:
    res = subprocess.run(["claude", "-p", prompt], capture_output=True, text=True, timeout=timeout)
    if res.returncode != 0:
        raise RuntimeError(f"claude -p rc={res.returncode}: {res.stderr[:400]}")
    return res.stdout.strip()


def parse_json(out: str) -> dict:
    t = re.sub(r"```$", "", re.sub(r"^```(?:json)?", "", out.strip()).strip()).strip()
    i, j = t.find("{"), t.rfind("}")
    if i == -1 or j == -1:
        raise ValueError(f"no JSON object in output: {out[:200]}")
    return json.loads(t[i : j + 1])


def _as_list(v) -> list[str]:
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    if isinstance(v, str) and v.strip():
        return [v.strip()]
    return []


def _as_bool(v, default: bool = True) -> bool:
    if isinstance(v, bool):  # bool は int のサブクラスなので数値判定より前に見る
        return v
    if isinstance(v, str):
        return v.strip().lower() in ("true", "yes", "1")
    if isinstance(v, (int, float)):  # LLM が 0/1 を返すケース（0=false を黙ってtrueにしない）
        return bool(v)
    return default


def write_case(row, data: dict) -> Path:
    # カバレッジ優先度: 非AI(ai_relevant=false)は概要＋汎用タグのみの軽量カードにする。
    # 深掘りファセット(patterns/components)と 設計/使いどころは AI関連のみ。
    ai_relevant = _as_bool(data.get("ai_relevant"), True)
    fm = {
        "type": data.get("type", "case"),
        "title": data.get("title", row["title"]),
        "title_original": data.get("title_original", row["title"]),
    }
    # 既定 true（スキーマ default）なので、軽量カード(false)のときだけ明示する＝既存フルカードの差分を出さない
    if not ai_relevant:
        fm["ai_relevant"] = False
    if (data.get("company") or "").strip():
        fm["company"] = data["company"].strip()
    if (data.get("industry") or "").strip():
        fm["industry"] = data["industry"].strip()
    fm["cloud"] = _as_list(data.get("cloud"))
    fm["patterns"] = _as_list(data.get("patterns")) if ai_relevant else []
    fm["components"] = _as_list(data.get("components")) if ai_relevant else []
    if ((data.get("outcome") or {}).get("type") or "").strip():
        fm["outcome"] = {"type": data["outcome"]["type"].strip()}
    fm["source_id"] = row["source_id"]
    fm["source_name"] = row["source_name"]
    fm["source_url"] = row["url"]
    # 公開日が抽出できなければ取得日(fetched_at)にフォールバック（空欄を作らない）
    fm["published_at"] = row["published"] or (row["fetched_at"] or "")[:10]
    if ai_relevant:
        # 設計のポイント・使いどころは markdown 箇条書き（配列）。後方互換で文字列(prose)も許容。
        def _bullets(v):
            if isinstance(v, list):
                return "\n".join(f"- {str(x).strip()}" for x in v if str(x).strip())
            return (v or "").strip()
        body = (
            f"## 概要\n\n{data.get('summary','').strip()}\n\n"
            f"## 設計のポイント\n\n{_bullets(data.get('design_point'))}\n\n"
            f"## 使いどころ\n\n{_bullets(data.get('use_case'))}\n"
        )
    else:
        body = f"## 概要\n\n{data.get('summary','').strip()}\n"
    front = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120).strip()
    CASES_DIR.mkdir(parents=True, exist_ok=True)
    path = CASES_DIR / f"{row['id']}.md"
    path.write_text(f"---\n{front}\n---\n\n{body}", encoding="utf-8")
    return path


def cmd_generate(args):
    con = db_connect()
    vocab = load_vocab()
    if args.dry_run:
        sql = """SELECT * FROM articles
                 WHERE status='fetched' AND text IS NOT NULL AND text!=''
                 ORDER BY published DESC, fetched_at ASC"""
        rows = con.execute(sql + (" LIMIT ?" if args.limit else ""), ((args.limit,) if args.limit else ())).fetchall()
    else:
        rows = claim_fetched(con, args.limit)
    done = 0
    for row in rows:
        if args.dry_run:
            log("  would generate", row["id"]); done += 1; continue
        try:
            data = parse_json(run_claude(build_prompt(row, vocab)))
            path = write_case(row, data)
        except Exception as e:
            con.execute(
                "UPDATE articles SET status='error', error=? WHERE id=? AND status='generating'",
                (str(e)[:300], row["id"]),
            )
            con.commit()
            log("  gen-fail", row["id"], type(e).__name__, str(e)[:160]); continue
        con.execute(
            """UPDATE articles
               SET status='generated', case_path=?, generated_at=?, error=NULL
               WHERE id=? AND status='generating'""",
            (str(path.relative_to(ROOT)), now_iso(), row["id"]),
        )
        con.commit()
        log("  wrote", f"cases/{row['id']}.md", "|", data.get("type"), "|", data.get("title", "")[:45])
        done += 1
    log(f"generate done: {done} case(s)")


def cmd_generate_emit(args):
    """fetched を claim（generating へ移す）し、生成プロンプトを JSONL で出力する。

    LLM は呼ばない（`claude -p` 非使用）。claude-job（tmux）内の Claude が各行の prompt を
    処理し、その結果を generate-ingest に渡す前提。1行 = {"id","source_name","url","prompt"}。
    claim 済み（generating）だが ingest されなかった記事は retry --include-generating で戻す。
    """
    con = db_connect()
    vocab = load_vocab()
    # 出力先を先に開いてから claim する。--out のパスが不正でも記事を generating に
    # 取り残さない（claim は commit 済みで巻き戻せないため、副作用は開けた後だけにする）。
    out = open(args.out, "w", encoding="utf-8") if args.out else sys.stdout
    n = 0
    try:
        rows = claim_fetched(con, args.limit)
        for row in rows:
            rec = {
                "id": row["id"],
                "source_name": row["source_name"],
                "url": row["url"],
                "prompt": build_prompt(row, vocab),
            }
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1
    finally:
        if args.out:
            out.close()
    log(f"generate-emit: claimed {n} article(s) → {args.out or 'stdout'}")


def _ingest_mark_error(con, aid: str, msg: str) -> None:
    con.execute(
        "UPDATE articles SET status='error', error=? WHERE id=? AND status='generating'",
        (msg[:300], aid),
    )
    con.commit()


def cmd_generate_ingest(args):
    """generate-emit で claim した記事に対する、セッション生成結果を取り込む。

    input（省略時 stdin）は JSONL。各行:
      {"id": <article id>, "data": {<事例カードJSON>}}   … 成功。data は dict でも文字列でも可。
      {"id": <article id>, "error": "<理由>"}            … セッション側で生成できなかった。
    generating の記事のみ対象（それ以外の id は無視）。write_case → generated、失敗は error。
    """
    con = db_connect()
    src = open(args.input, encoding="utf-8") if args.input else sys.stdin
    ok = err = skipped = 0
    try:
        for line in src:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except Exception as e:
                log("  ingest: bad JSONL line", type(e).__name__, str(e)[:120]); skipped += 1; continue
            aid = rec.get("id")
            if not aid:
                log("  ingest: line without id, skip"); skipped += 1; continue
            row = con.execute(
                "SELECT * FROM articles WHERE id=? AND status='generating'", (aid,)
            ).fetchone()
            if row is None:
                log("  ingest: not in generating, skip", aid); skipped += 1; continue
            if rec.get("error") or "data" not in rec:
                msg = str(rec.get("error") or "no data in ingest record")
                _ingest_mark_error(con, aid, msg)
                log("  gen-fail", aid, msg[:120]); err += 1; continue
            try:
                data = rec["data"]
                if isinstance(data, str):
                    data = parse_json(data)
                if not isinstance(data, dict):
                    raise ValueError(f"data is {type(data).__name__}, expected object")
                # 空/退化データ（summary も title も無い）を generated として書き出さない。
                # ingest は無人公開経路のため、最低限の中身が無ければ error に落とす。
                if not (str(data.get("summary", "")).strip() or str(data.get("title", "")).strip()):
                    raise ValueError("empty case data (no summary/title)")
                path = write_case(row, data)
            except Exception as e:
                _ingest_mark_error(con, aid, f"{type(e).__name__}: {e}")
                log("  gen-fail", aid, type(e).__name__, str(e)[:160]); err += 1; continue
            con.execute(
                """UPDATE articles
                   SET status='generated', case_path=?, generated_at=?, error=NULL
                   WHERE id=? AND status='generating'""",
                (str(path.relative_to(ROOT)), now_iso(), aid),
            )
            con.commit()
            log("  wrote", f"cases/{aid}.md", "|", data.get("type"), "|", str(data.get("title", ""))[:45])
            ok += 1
    finally:
        if args.input:
            src.close()
    log(f"generate-ingest done: {ok} written, {err} error(s), {skipped} skipped")


def cmd_retry(args):
    con = db_connect()
    statuses = ["error"]
    if args.include_generating:
        statuses.append("generating")
    placeholders = ",".join("?" for _ in statuses)
    sql = f"SELECT id FROM articles WHERE status IN ({placeholders}) ORDER BY last_attempt_at ASC"
    params: list = list(statuses)
    if args.limit:
        sql += " LIMIT ?"
        params.append(args.limit)
    ids = [r["id"] for r in con.execute(sql, params)]
    if ids:
        marks = ",".join("?" for _ in ids)
        con.execute(
            f"UPDATE articles SET status='fetched', error=NULL WHERE id IN ({marks})",
            ids,
        )
        con.commit()
    print(f"retry queued: {len(ids)} article(s)")


def cmd_status(args):
    con = db_connect()
    total = con.execute("SELECT COUNT(*) FROM articles").fetchone()[0]
    print(f"台帳: {DB_PATH.relative_to(ROOT)}  総記事 {total}")
    print("--- status別 ---")
    for r in con.execute("SELECT status, COUNT(*) n FROM articles GROUP BY status ORDER BY n DESC"):
        print(f"  {r['status']:12} {r['n']}")
    print("--- source別（未生成 fetched を含む）---")
    for r in con.execute(
        """SELECT source_id,
                  SUM(status='fetched') fetched, SUM(status='generated') generated,
                  SUM(status='generating') generating, SUM(status='error') err, COUNT(*) total
           FROM articles GROUP BY source_id ORDER BY total DESC"""
    ):
        print(
            f"  {r['source_id']:34} fetched={r['fetched']:<3} generating={r['generating']:<3} "
            f"generated={r['generated']:<3} error={r['err']:<2} total={r['total']}"
        )


def cmd_run(args):
    cmd_fetch(args)
    args.limit = args.generate_limit
    cmd_generate(args)


def positive_int(value: str) -> int:
    n = int(value)
    if n <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return n


def main():
    ap = argparse.ArgumentParser(description="ai-architecture-digest collector (SQLite 台帳)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pf = sub.add_parser("fetch")
    pf.add_argument("--source")
    pf.add_argument("--max-new-per-source", "--limit", dest="max_new_per_source", type=positive_int, default=50)
    pf.add_argument("--max-total", type=positive_int, default=500)
    pf.add_argument("--max-fetch", type=positive_int, default=100)
    pf.add_argument("--dry-run", action="store_true")
    pf.set_defaults(func=cmd_fetch)
    pg = sub.add_parser("generate")
    pg.add_argument("--limit", type=positive_int, default=3)
    pg.add_argument("--dry-run", action="store_true")
    pg.set_defaults(func=cmd_generate)
    pe = sub.add_parser("generate-emit")
    pe.add_argument("--limit", type=positive_int, default=30)
    pe.add_argument("--out")
    pe.set_defaults(func=cmd_generate_emit)
    pi = sub.add_parser("generate-ingest")
    pi.add_argument("--input")
    pi.set_defaults(func=cmd_generate_ingest)
    sub.add_parser("status").set_defaults(func=cmd_status)
    pt = sub.add_parser("retry")
    pt.add_argument("--limit", type=positive_int, default=0)
    pt.add_argument("--include-generating", action="store_true")
    pt.set_defaults(func=cmd_retry)
    pr = sub.add_parser("run")
    pr.add_argument("--source")
    pr.add_argument("--max-new-per-source", "--limit", dest="max_new_per_source", type=positive_int, default=50)
    pr.add_argument("--max-total", type=positive_int, default=500)
    pr.add_argument("--max-fetch", type=positive_int, default=100)
    pr.add_argument("--generate-limit", type=positive_int, default=3)
    pr.add_argument("--dry-run", action="store_true")
    pr.set_defaults(func=cmd_run)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
