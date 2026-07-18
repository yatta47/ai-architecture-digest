#!/usr/bin/env python3
"""ai-architecture-digest collector.

状態は SQLite（scripts/.cache/collect.db）の articles 台帳で一元管理する。
  status: fetched（取得済み・未生成） / generated（事例MD生成済み） / error

2 段構え（ローカル実行前提）:
  fetch    : sources.yml の各ソースから新着を取得 → articles に status='fetched' で登録（決定的・LLM不要）
  generate : status='fetched' の記事を `claude -p` に渡して事例MDを作る → src/content/cases/<id>.md、status='generated'
  status   : 台帳サマリ（status別・source別件数）を表示

取得方式:
  - rss                : RSS を parse（stdlib）→ 本文は bs4 抽出
  - sitemap / page-diff: ソース別 discovery（catalog ロジックを移植・自己完結）でURL列挙 → 各ページから title/date/text
  - manual             : 自動取得不可（robots.txt 等）。スキップ

設計:
  - 生成は claude CLI（サブスク認証・APIキー不要）。1記事=1呼び出し、ローカルでコスト管理。
  - 冪等: URL が台帳 or 既存 case md にあればスキップ。
  - 語彙は vocab/*.yml を prompt に渡して寄せる（無ければ新語可）。
使い方:
  python scripts/collect.py fetch [--source ID] [--limit N] [--max-fetch M] [--dry-run]
  python scripts/collect.py generate [--limit N] [--dry-run]
  python scripts/collect.py status
  python scripts/collect.py run [--source ID] [--limit N]
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
            case_path TEXT, fetched_at TEXT, generated_at TEXT, error TEXT)"""
    )
    con.execute("CREATE INDEX IF NOT EXISTS idx_status ON articles(status)")
    con.execute("CREATE INDEX IF NOT EXISTS idx_source ON articles(source_id)")
    # 既存の committed な case md を台帳へ取り込む（DBを消しても重複生成しないため）
    known = {r[0] for r in con.execute("SELECT url FROM articles")}
    for p in CASES_DIR.glob("*.md"):
        txt = p.read_text(encoding="utf-8")
        m = re.search(r"^source_url:\s*(\S+)", txt, re.M)
        if not m:
            continue
        url = m.group(1).strip()
        if url in known:
            continue
        con.execute(
            "INSERT OR IGNORE INTO articles(id,url,source_id,status,case_path,generated_at) VALUES(?,?,?,?,?,?)",
            (p.stem, url, _fm_field(txt, "source_id"), "generated", str(p.relative_to(ROOT)), now_iso()),
        )
    con.commit()
    return con


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
    for sm in subs:
        try:
            xml = fetch_bytes(sm).decode("utf-8", errors="ignore")
        except Exception as e:
            log("  fail-sitemap", sm, type(e).__name__); continue
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


def discover_gcp_architecture_center() -> list[dict]:
    # docs.cloud.google.com/sitemap.xml（60分割 gzip）→ /architecture/。lastmod無し（日付はページから補完）。
    idx = fetch_bytes("https://docs.cloud.google.com/sitemap.xml").decode("utf-8", errors="ignore")
    out, seen = [], set()
    for sm in LOC_RE.findall(idx):
        try:
            raw = fetch_bytes(sm)
        except Exception as e:
            log("  fail-sitemap", sm, type(e).__name__); continue
        if raw[:2] == b"\x1f\x8b":
            raw = gzip.decompress(raw)
        for loc in LOC_RE.findall(raw.decode("utf-8", errors="ignore")):
            if "/architecture/" in loc and "hl=" not in loc and loc not in seen:
                seen.add(loc); out.append({"url": loc})
        if len(out) >= 200:  # 早期打ち切り（全60分割は重い・日付が無く順序も任意のため）
            break
    return out


DISCOVERERS = {
    "claude-blog": discover_claude_blog,
    "llamaindex-blog": discover_llamaindex_blog,
    "aws-architecture-center": discover_aws_architecture_center,
    "azure-architecture-center": discover_azure_architecture_center,
    "google-cloud-architecture-center": discover_gcp_architecture_center,
}


# ================= fetch =================
def _fetch_rss(con, s, args) -> int:
    try:
        feed = parse_feed(fetch_bytes(s["url"]))
    except Exception as e:
        log("skip", s["id"], type(e).__name__, e); return 0
    feed.sort(key=lambda x: x["date"], reverse=True)
    added = 0
    for it in feed[: args.limit]:
        if not it["link"] or not it["title"] or is_non_article(it["link"]) or db_has_url(con, it["link"]):
            continue
        if args.dry_run:
            log("  would add", it["title"][:60]); continue
        try:
            text = extract_text(it["link"])
        except Exception as e:
            log("  text-fail", it["link"], type(e).__name__); text = ""
        if db_insert_fetched(con, s, it["title"], it["link"], it["date"], text):
            added += 1
    return added


def _fetch_nonrss(con, s, args) -> int:
    try:
        items = DISCOVERERS[s["id"]]()
    except Exception as e:
        log("skip", s["id"], type(e).__name__, e); return 0
    fresh = [it for it in items if not db_has_url(con, it["url"]) and not is_non_article(it["url"])][: (args.max_fetch or 30)]
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
    for title, u, date, text in got[: args.limit]:
        if args.dry_run:
            log("  would add", title[:55], date); continue
        if db_insert_fetched(con, s, title, u, date, text):
            added += 1
    return added


def cmd_fetch(args):
    con = db_connect()
    sel = [s for s in load_sources() if (not args.source or s["id"] == args.source)]
    added = 0
    for s in sel:
        if s.get("method") == "rss":
            added += _fetch_rss(con, s, args)
        elif s["id"] in DISCOVERERS:
            added += _fetch_nonrss(con, s, args)
        elif args.source:
            log(f"  (no auto-fetch for method={s.get('method')}: {s['id']})")
    log(f"fetch done: {added} new article(s)")


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
  "title": "日本語の再構成タイトル（記事名の直訳でなく『何のシステム/話か』を一言で）",
  "title_original": "元記事タイトル（英語のまま）",
  "company": "実装主体の企業名。無ければ空文字",
  "industry": "industriesから1つ。該当なければ cross-industry",
  "cloud": ["cloudから該当するもの（複数可・無ければ空配列）"],
  "patterns": ["patternsから該当するもの1〜4個"],
  "components": ["記事に出てくる具体的なサービス/製品名（例: Amazon Bedrock, OpenSearch）。無ければ空配列"],
  "data_sources": ["システムが扱うデータ種別の短い語。無ければ空配列"],
  "outcome": {{"type": "outcomesから1つ"}},
  "summary": "『## 概要』に入れる2〜3文の日本語要約",
  "design_point": "『## 設計のポイント』に入れる、再利用できる設計判断を2〜3文",
  "use_case": "『## 使いどころ』に入れる、どんな場面・人に効くかを1〜2文"
}}

判定の指針:
- type: 具体的な実装事例=case / 手引き・リファレンス=guidance / 意見・考察=opinion / 提供開始・機能告知=announcement
- 具体的な構成が読み取れない記事でも type で分類して出す（事例以外は company/components が空でよい）

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


def write_case(row, data: dict) -> Path:
    fm = {
        "type": data.get("type", "case"),
        "title": data.get("title", row["title"]),
        "title_original": data.get("title_original", row["title"]),
    }
    if (data.get("company") or "").strip():
        fm["company"] = data["company"].strip()
    if (data.get("industry") or "").strip():
        fm["industry"] = data["industry"].strip()
    fm["cloud"] = _as_list(data.get("cloud"))
    fm["patterns"] = _as_list(data.get("patterns"))
    fm["components"] = _as_list(data.get("components"))
    fm["data_sources"] = _as_list(data.get("data_sources"))
    if ((data.get("outcome") or {}).get("type") or "").strip():
        fm["outcome"] = {"type": data["outcome"]["type"].strip()}
    fm["source_id"] = row["source_id"]
    fm["source_name"] = row["source_name"]
    fm["source_url"] = row["url"]
    # 公開日が抽出できなければ取得日(fetched_at)にフォールバック（空欄を作らない）
    fm["published_at"] = row["published"] or (row["fetched_at"] or "")[:10]
    body = (
        f"## 概要\n\n{data.get('summary','').strip()}\n\n"
        f"## 設計のポイント\n\n{data.get('design_point','').strip()}\n\n"
        f"## 使いどころ\n\n{data.get('use_case','').strip()}\n"
    )
    front = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120).strip()
    CASES_DIR.mkdir(parents=True, exist_ok=True)
    path = CASES_DIR / f"{row['id']}.md"
    path.write_text(f"---\n{front}\n---\n\n{body}", encoding="utf-8")
    return path


def cmd_generate(args):
    con = db_connect()
    vocab = load_vocab()
    rows = con.execute(
        "SELECT * FROM articles WHERE status='fetched' AND text IS NOT NULL AND text!='' ORDER BY published DESC"
    ).fetchall()
    done = 0
    for row in rows:
        if args.limit and done >= args.limit:
            break
        if args.dry_run:
            log("  would generate", row["id"]); done += 1; continue
        try:
            data = parse_json(run_claude(build_prompt(row, vocab)))
        except Exception as e:
            con.execute("UPDATE articles SET status='error', error=? WHERE id=?", (str(e)[:300], row["id"]))
            con.commit()
            log("  gen-fail", row["id"], type(e).__name__, str(e)[:160]); continue
        path = write_case(row, data)
        con.execute(
            "UPDATE articles SET status='generated', case_path=?, generated_at=? WHERE id=?",
            (str(path.relative_to(ROOT)), now_iso(), row["id"]),
        )
        con.commit()
        log("  wrote", f"cases/{row['id']}.md", "|", data.get("type"), "|", data.get("title", "")[:45])
        done += 1
    log(f"generate done: {done} case(s)")


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
                  SUM(status='error') err, COUNT(*) total
           FROM articles GROUP BY source_id ORDER BY total DESC"""
    ):
        print(f"  {r['source_id']:34} fetched={r['fetched']:<3} generated={r['generated']:<3} error={r['err']:<2} total={r['total']}")


def cmd_run(args):
    cmd_fetch(args)
    cmd_generate(args)


def main():
    ap = argparse.ArgumentParser(description="ai-architecture-digest collector (SQLite 台帳)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pf = sub.add_parser("fetch")
    pf.add_argument("--source"); pf.add_argument("--limit", type=int, default=5)
    pf.add_argument("--max-fetch", type=int, default=30); pf.add_argument("--dry-run", action="store_true")
    pf.set_defaults(func=cmd_fetch)
    pg = sub.add_parser("generate")
    pg.add_argument("--limit", type=int, default=0); pg.add_argument("--dry-run", action="store_true")
    pg.set_defaults(func=cmd_generate)
    sub.add_parser("status").set_defaults(func=cmd_status)
    pr = sub.add_parser("run")
    pr.add_argument("--source"); pr.add_argument("--limit", type=int, default=3)
    pr.add_argument("--max-fetch", type=int, default=30); pr.add_argument("--dry-run", action="store_true")
    pr.set_defaults(func=cmd_run)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
