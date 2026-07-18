#!/usr/bin/env python3
"""ai-architecture-digest collector.

2 段構え（ローカル実行前提）:
  fetch    : sources.yml の RSS から新着を取得 → scripts/.cache/candidates/<id>.json（決定的・LLM不要）
  generate : 未生成の candidate を `claude -p` に渡して事例MDを作る → src/content/cases/<id>.md

設計:
  - 生成は claude CLI（サブスク認証・APIキー不要）。1記事=1呼び出し、ローカルでコスト管理。
  - 冪等: 既に case md / candidate がある id はスキップ。
  - 語彙は vocab/*.yml を prompt に渡して寄せる（無ければ新語可・後で辞書へ）。
使い方:
  python scripts/collect.py fetch --source aws-machine-learning-blog --limit 3
  python scripts/collect.py generate --limit 1
  python scripts/collect.py run          # fetch 全ソース → generate 全件
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
SOURCES_FILE = ROOT / "sources.yml"
VOCAB_DIR = ROOT / "vocab"
CACHE_DIR = SCRIPT_DIR / ".cache" / "candidates"
CASES_DIR = ROOT / "src" / "content" / "cases"
UA = "Mozilla/5.0 (compatible; ai-architecture-digest/0.1)"


def log(*a):
    print(*a, file=sys.stderr)


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


# ---------- RSS / Atom parsing (namespace-agnostic) ----------
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
                rel = child.get("rel")
                href = child.get("href")
                if href and (rel in (None, "alternate")) and not link:
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
    try:
        return parsedate_to_datetime(s).date().isoformat()
    except Exception:
        pass
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).date().isoformat()
    except Exception:
        return ""


def extract_text(url: str, limit: int = 8000) -> str:
    html = fetch_bytes(url).decode("utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(["script", "style", "nav", "header", "footer", "aside", "form"]):
        t.decompose()
    main = soup.find("main") or soup.find("article") or soup.body or soup
    text = main.get_text(" ", strip=True)
    return re.sub(r"\s+", " ", text)[:limit]


def case_ids() -> set[str]:
    return {p.stem for p in CASES_DIR.glob("*.md")}


def candidate_ids() -> set[str]:
    return {p.stem for p in CACHE_DIR.glob("*.json")}


# ---------- fetch ----------
def cmd_fetch(args):
    sources = [
        s
        for s in load_sources()
        if s.get("method") == "rss" and (not args.source or s["id"] == args.source)
    ]
    if not sources:
        log("no matching rss source"); return
    seen = case_ids() | candidate_ids()
    added = 0
    for s in sources:
        try:
            feed = parse_feed(fetch_bytes(s["url"]))
        except Exception as e:
            log("skip", s["id"], type(e).__name__, e); continue
        feed.sort(key=lambda x: x["date"], reverse=True)
        for it in feed[: args.limit]:
            if not it["link"] or not it["title"]:
                continue
            cid = f'{s["id"]}-{slugify(it["title"])[:60]}'
            if cid in seen:
                continue
            if args.dry_run:
                log("  would add", cid, "|", it["title"][:60]); continue
            try:
                text = extract_text(it["link"])
            except Exception as e:
                log("  text-fail", it["link"], type(e).__name__); text = ""
            cand = {
                "id": cid, "title": it["title"], "link": it["link"], "published": it["date"],
                "source_id": s["id"], "source_name": s["name"], "tier": s.get("tier"),
                "vendors": s.get("vendors", []), "text": text,
            }
            CACHE_DIR.mkdir(parents=True, exist_ok=True)
            (CACHE_DIR / f"{cid}.json").write_text(json.dumps(cand, ensure_ascii=False, indent=2), encoding="utf-8")
            seen.add(cid); added += 1
            log("  +", cid)
    log(f"fetch done: {added} candidate(s)")


# ---------- generate ----------
def load_vocab() -> dict:
    v = {}
    for name in ["patterns", "cloud", "industries", "outcomes", "types"]:
        d = yaml.safe_load((VOCAB_DIR / f"{name}.yml").read_text(encoding="utf-8"))
        v[name] = list(d.values())[0]
    return v


def build_prompt(cand: dict, vocab: dict) -> str:
    return f"""あなたはAIアーキテクチャ事例カタログの編集者です。以下の記事から日本語の「事例カード」を1件作ります。
出力は **JSONオブジェクトのみ**（コードフェンス無し・前後に説明文を付けない）。

記事メタ:
- source_name: {cand['source_name']}
- source_url: {cand['link']}
- published_at: {cand['published']}

記事本文（抜粋・整形済み）:
\"\"\"
{cand['text'][:7000]}
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
    t = out.strip()
    t = re.sub(r"^```(?:json)?", "", t).strip()
    t = re.sub(r"```$", "", t).strip()
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


def write_case(cand: dict, data: dict):
    fm = {
        "type": data.get("type", "case"),
        "title": data.get("title", cand["title"]),
        "title_original": data.get("title_original", cand["title"]),
    }
    company = (data.get("company") or "").strip()
    if company:
        fm["company"] = company
    industry = (data.get("industry") or "").strip()
    if industry:
        fm["industry"] = industry
    fm["cloud"] = _as_list(data.get("cloud"))
    fm["patterns"] = _as_list(data.get("patterns"))
    fm["components"] = _as_list(data.get("components"))
    fm["data_sources"] = _as_list(data.get("data_sources"))
    otype = ((data.get("outcome") or {}).get("type") or "").strip()
    if otype:
        fm["outcome"] = {"type": otype}
    fm["source_id"] = cand["source_id"]
    fm["source_name"] = cand["source_name"]
    fm["source_url"] = cand["link"]
    fm["published_at"] = cand["published"] or ""

    body = (
        f"## 概要\n\n{data.get('summary','').strip()}\n\n"
        f"## 設計のポイント\n\n{data.get('design_point','').strip()}\n\n"
        f"## 使いどころ\n\n{data.get('use_case','').strip()}\n"
    )
    front = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120).strip()
    md = f"---\n{front}\n---\n\n{body}"
    CASES_DIR.mkdir(parents=True, exist_ok=True)
    (CASES_DIR / f"{cand['id']}.md").write_text(md, encoding="utf-8")


def cmd_generate(args):
    vocab = load_vocab()
    existing = case_ids()
    cands = sorted(CACHE_DIR.glob("*.json"))
    done = 0
    for p in cands:
        if args.limit and done >= args.limit:
            break
        cand = json.loads(p.read_text(encoding="utf-8"))
        if cand["id"] in existing:
            continue
        if not cand.get("text"):
            log("  no-text, skip", cand["id"]); continue
        if args.dry_run:
            log("  would generate", cand["id"]); done += 1; continue
        try:
            data = parse_json(run_claude(build_prompt(cand, vocab)))
        except Exception as e:
            log("  gen-fail", cand["id"], type(e).__name__, str(e)[:200]); continue
        write_case(cand, data)
        log("  wrote", f"src/content/cases/{cand['id']}.md", "|", data.get("type"), "|", data.get("title", "")[:50])
        done += 1
    log(f"generate done: {done} case(s)")


def cmd_run(args):
    cmd_fetch(args)
    cmd_generate(args)


def main():
    ap = argparse.ArgumentParser(description="ai-architecture-digest collector")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pf = sub.add_parser("fetch"); pf.add_argument("--source"); pf.add_argument("--limit", type=int, default=5); pf.add_argument("--dry-run", action="store_true"); pf.set_defaults(func=cmd_fetch)
    pg = sub.add_parser("generate"); pg.add_argument("--limit", type=int, default=0); pg.add_argument("--dry-run", action="store_true"); pg.set_defaults(func=cmd_generate)
    pr = sub.add_parser("run"); pr.add_argument("--source"); pr.add_argument("--limit", type=int, default=3); pr.add_argument("--dry-run", action="store_true"); pr.set_defaults(func=cmd_run)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
