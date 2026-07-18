import contextlib
import importlib.util
import io
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


SPEC = importlib.util.spec_from_file_location(
    "collector", Path(__file__).parents[1] / "scripts" / "collect.py"
)
collector = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(collector)


class CollectorTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.cases = self.root / "src" / "content" / "cases"
        self.cases.mkdir(parents=True)
        self.db_path = self.root / "scripts" / ".cache" / "collect.db"
        self.old_globals = (collector.ROOT, collector.CASES_DIR, collector.DB_PATH)
        collector.ROOT = self.root
        collector.CASES_DIR = self.cases
        collector.DB_PATH = self.db_path

    def tearDown(self):
        collector.ROOT, collector.CASES_DIR, collector.DB_PATH = self.old_globals
        self.tmp.cleanup()

    def test_db_connect_migrates_and_repairs_existing_markdown(self):
        self.db_path.parent.mkdir(parents=True)
        con = sqlite3.connect(self.db_path)
        con.execute(
            """CREATE TABLE articles(
                id TEXT PRIMARY KEY, url TEXT UNIQUE NOT NULL,
                source_id TEXT, source_name TEXT, tier TEXT,
                title TEXT, published TEXT, text TEXT, vendors TEXT,
                status TEXT NOT NULL DEFAULT 'fetched',
                case_path TEXT, fetched_at TEXT, generated_at TEXT, error TEXT)"""
        )
        con.execute(
            "INSERT INTO articles(id,url,source_id,status,text) VALUES(?,?,?,?,?)",
            ("case-1", "https://example.com/1", "example", "fetched", "body"),
        )
        con.commit()
        con.close()
        (self.cases / "case-1.md").write_text(
            "---\nsource_id: example\nsource_url: https://example.com/1\n---\n",
            encoding="utf-8",
        )

        con = collector.db_connect()

        row = con.execute(
            "SELECT status,case_path,retry_count,last_attempt_at FROM articles WHERE id='case-1'"
        ).fetchone()
        self.assertEqual(row["status"], "generated")
        self.assertEqual(row["case_path"], "src/content/cases/case-1.md")
        self.assertEqual(row["retry_count"], 0)
        self.assertIsNone(row["last_attempt_at"])

    def test_rss_scans_past_known_items_and_respects_new_limit(self):
        con = collector.db_connect()
        con.execute(
            "INSERT INTO articles(id,url,status) VALUES(?,?,?)",
            ("known", "https://example.com/known", "generated"),
        )
        con.commit()
        feed = b"""<rss><channel>
          <item><title>Known</title><link>https://example.com/known</link><pubDate>Sat, 19 Jul 2026 00:00:00 GMT</pubDate></item>
          <item><title>New One</title><link>https://example.com/1</link><pubDate>Fri, 18 Jul 2026 00:00:00 GMT</pubDate></item>
          <item><title>New Two</title><link>https://example.com/2</link><pubDate>Thu, 17 Jul 2026 00:00:00 GMT</pubDate></item>
          <item><title>New Three</title><link>https://example.com/3</link><pubDate>Wed, 16 Jul 2026 00:00:00 GMT</pubDate></item>
        </channel></rss>"""
        args = SimpleNamespace(max_new_per_source=2, dry_run=False)
        source = {
            "id": "example",
            "name": "Example",
            "tier": "tier1",
            "url": "https://example.com/feed.xml",
            "vendors": [],
        }

        with mock.patch.object(collector, "fetch_bytes", return_value=feed), mock.patch.object(
            collector, "extract_text", return_value="article body"
        ):
            added = collector._fetch_rss(con, source, args, remaining=10)

        self.assertEqual(added, 2)
        urls = {r[0] for r in con.execute("SELECT url FROM articles")}
        self.assertIn("https://example.com/1", urls)
        self.assertIn("https://example.com/2", urls)
        self.assertNotIn("https://example.com/3", urls)

    def test_claim_is_exclusive_and_records_attempt(self):
        con = collector.db_connect()
        for n in range(2):
            con.execute(
                """INSERT INTO articles(id,url,status,text,published,fetched_at)
                   VALUES(?,?,?,?,?,?)""",
                (f"case-{n}", f"https://example.com/{n}", "fetched", "body", f"2026-07-1{n}", f"2026-07-1{n}"),
            )
        con.commit()

        first = collector.claim_fetched(con, 1)
        second = collector.claim_fetched(con, 1)

        self.assertEqual(len(first), 1)
        self.assertEqual(len(second), 1)
        self.assertNotEqual(first[0]["id"], second[0]["id"])
        rows = con.execute("SELECT status,retry_count,last_attempt_at FROM articles").fetchall()
        self.assertTrue(all(r["status"] == "generating" for r in rows))
        self.assertTrue(all(r["retry_count"] == 1 for r in rows))
        self.assertTrue(all(r["last_attempt_at"] for r in rows))

    def test_fetch_respects_per_source_and_total_limits(self):
        sources = [
            {"id": f"source-{n}", "name": f"Source {n}", "method": "rss", "url": f"https://example.com/{n}"}
            for n in range(3)
        ]
        args = SimpleNamespace(
            source=None,
            max_new_per_source=5,
            max_total=7,
            max_fetch=100,
            dry_run=False,
        )
        remaining_seen = []

        def fake_fetch(_con, _source, call_args, remaining):
            remaining_seen.append(remaining)
            return min(call_args.max_new_per_source, remaining)

        with mock.patch.object(collector, "db_connect", return_value=object()), mock.patch.object(
            collector, "load_sources", return_value=sources
        ), mock.patch.object(collector, "_fetch_rss", side_effect=fake_fetch):
            collector.cmd_fetch(args)

        self.assertEqual(remaining_seen, [7, 2])

    def test_retry_requeues_errors_and_optionally_stale_generating(self):
        con = collector.db_connect()
        con.executemany(
            "INSERT INTO articles(id,url,status,text) VALUES(?,?,?,?)",
            [
                ("error", "https://example.com/error", "error", "body"),
                ("generating", "https://example.com/generating", "generating", "body"),
            ],
        )
        con.commit()
        con.close()

        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            collector.cmd_retry(SimpleNamespace(limit=0, include_generating=False))
        con = collector.db_connect()
        states = dict(con.execute("SELECT id,status FROM articles"))
        self.assertEqual(states, {"error": "fetched", "generating": "generating"})

        with contextlib.redirect_stdout(out):
            collector.cmd_retry(SimpleNamespace(limit=0, include_generating=True))
        states = dict(con.execute("SELECT id,status FROM articles"))
        self.assertEqual(states, {"error": "fetched", "generating": "fetched"})


    def test_generate_emit_claims_fetched_and_writes_prompts(self):
        con = collector.db_connect()
        con.executemany(
            """INSERT INTO articles(id,url,source_id,source_name,status,text,published,fetched_at)
               VALUES(?,?,?,?,?,?,?,?)""",
            [
                ("case-0", "https://example.com/0", "example", "Example", "fetched",
                 "body zero", "2026-07-10", "2026-07-10"),
                ("case-1", "https://example.com/1", "example", "Example", "fetched",
                 "body one", "2026-07-11", "2026-07-11"),
            ],
        )
        con.commit()
        con.close()

        out_path = self.root / "prompts.jsonl"
        with contextlib.redirect_stderr(io.StringIO()):
            collector.cmd_generate_emit(SimpleNamespace(limit=30, out=str(out_path)))

        lines = [json.loads(l) for l in out_path.read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertEqual({r["id"] for r in lines}, {"case-0", "case-1"})
        self.assertTrue(all("prompt" in r and r["prompt"] for r in lines))
        # プロンプトには記事の source_url が埋まっている
        by_id = {r["id"]: r for r in lines}
        self.assertIn("https://example.com/0", by_id["case-0"]["prompt"])

        con = collector.db_connect()
        states = dict(con.execute("SELECT id,status FROM articles"))
        self.assertEqual(states, {"case-0": "generating", "case-1": "generating"})

    def _insert_generating(self, con, aid="case-0", url="https://example.com/0"):
        con.execute(
            """INSERT INTO articles(id,url,source_id,source_name,tier,title,published,text,status,fetched_at)
               VALUES(?,?,?,?,?,?,?,?,?,?)""",
            (aid, url, "example", "Example", "tier1", "Orig Title", "2026-07-11",
             "body", "generating", "2026-07-11"),
        )
        con.commit()

    def test_generate_ingest_writes_case_and_marks_generated(self):
        con = collector.db_connect()
        self._insert_generating(con)
        con.close()

        data = {
            "type": "case", "ai_relevant": True,
            "title": "テストシステム", "title_original": "Test System",
            "company": "ACME", "industry": "cross-industry",
            "cloud": ["AWS"], "patterns": ["RAG"], "components": ["Amazon Bedrock"],
            "outcome": {"type": "cost-reduction"},
            "summary": "概要文です。", "design_point": ["設計判断1"], "use_case": ["用途1"],
        }
        in_path = self.root / "results.jsonl"
        in_path.write_text(json.dumps({"id": "case-0", "data": data}) + "\n", encoding="utf-8")

        with contextlib.redirect_stderr(io.StringIO()):
            collector.cmd_generate_ingest(SimpleNamespace(input=str(in_path)))

        con = collector.db_connect()
        row = con.execute("SELECT status,case_path FROM articles WHERE id='case-0'").fetchone()
        self.assertEqual(row["status"], "generated")
        self.assertEqual(row["case_path"], "src/content/cases/case-0.md")
        md = (self.cases / "case-0.md").read_text(encoding="utf-8")
        self.assertIn("テストシステム", md)
        self.assertIn("## 設計のポイント", md)

    def test_generate_ingest_accepts_data_as_json_string(self):
        con = collector.db_connect()
        self._insert_generating(con)
        con.close()

        payload = "```json\n" + json.dumps(
            {"type": "opinion", "ai_relevant": False, "title": "考察", "summary": "概要"}
        ) + "\n```"
        in_path = self.root / "results.jsonl"
        in_path.write_text(json.dumps({"id": "case-0", "data": payload}) + "\n", encoding="utf-8")

        with contextlib.redirect_stderr(io.StringIO()):
            collector.cmd_generate_ingest(SimpleNamespace(input=str(in_path)))

        con = collector.db_connect()
        self.assertEqual(
            con.execute("SELECT status FROM articles WHERE id='case-0'").fetchone()["status"],
            "generated",
        )

    def test_generate_ingest_rejects_empty_data(self):
        con = collector.db_connect()
        self._insert_generating(con)
        con.close()

        in_path = self.root / "results.jsonl"
        in_path.write_text(json.dumps({"id": "case-0", "data": {}}) + "\n", encoding="utf-8")

        with contextlib.redirect_stderr(io.StringIO()):
            collector.cmd_generate_ingest(SimpleNamespace(input=str(in_path)))

        con = collector.db_connect()
        self.assertEqual(
            con.execute("SELECT status FROM articles WHERE id='case-0'").fetchone()["status"],
            "error",
        )
        self.assertFalse((self.cases / "case-0.md").exists())

    def test_generate_ingest_marks_error_and_skips_non_generating(self):
        con = collector.db_connect()
        self._insert_generating(con, "err-explicit", "https://example.com/e1")
        self._insert_generating(con, "err-baddata", "https://example.com/e2")
        con.execute(
            "INSERT INTO articles(id,url,status) VALUES(?,?,?)",
            ("already", "https://example.com/a", "generated"),
        )
        con.commit()
        con.close()

        lines = [
            {"id": "err-explicit", "error": "session could not generate"},
            {"id": "err-baddata", "data": "not a json object"},
            {"id": "already", "data": {"type": "case", "summary": "x"}},  # not generating → skip
            {"id": "missing", "data": {"type": "case", "summary": "x"}},  # unknown id → skip
        ]
        in_path = self.root / "results.jsonl"
        in_path.write_text("\n".join(json.dumps(x) for x in lines) + "\n", encoding="utf-8")

        with contextlib.redirect_stderr(io.StringIO()):
            collector.cmd_generate_ingest(SimpleNamespace(input=str(in_path)))

        con = collector.db_connect()
        states = dict(con.execute("SELECT id,status FROM articles"))
        self.assertEqual(states["err-explicit"], "error")
        self.assertEqual(states["err-baddata"], "error")
        self.assertEqual(states["already"], "generated")  # 変化なし
        self.assertNotIn("missing", states)  # 作られない


if __name__ == "__main__":
    unittest.main()
