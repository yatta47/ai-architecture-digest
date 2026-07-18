# ai-architecture-digest

追跡ソース（AIアーキテクチャ関連ブログ／ドキュメント）の新着を、
**クラウド・パターン・業界・技術スタック・企業・成果**で引ける事例カタログ。

- SSG: Astro（1事例 = 1 Markdown → 個別URL + RSS）
- データ: `src/content/cases/*.md`（`scripts/collect.py` がローカル生成）
- 公開: [GitHub Pages](https://yatta47.github.io/ai-architecture-digest/)
- 計測: GA4（`G-7XTD8QLYTM`）→ BigQuery日次Export

計画: `ai-architecture-catalog/docs/20260718-digest-public-ga4-bigquery-plan.md`

## 開発

```bash
npm install
npm run build      # dist/ に静的出力
npm run dev        # 開発サーバ
```

BigQueryの確認・学習用SQLは [`docs/ga4-bigquery-guide.md`](docs/ga4-bigquery-guide.md) を参照。

## 記事の収集と生成

収集と生成はSQLite台帳を介した独立ジョブとして実行する。収集は新着を広く蓄積し、LLM生成は少数ずつ処理する。

```bash
# 全自動ソースから、1ソース最大50件・全体最大500件を取得
python scripts/collect.py fetch

# 待機中の記事を3件だけ生成
python scripts/collect.py generate --limit 3

# 台帳の待機・処理中・生成済み・エラー件数を確認
python scripts/collect.py status

# エラー記事を待機キューへ戻す
python scripts/collect.py retry
```

一括実行する場合も、取得上限と生成上限は別々に指定する。

```bash
python scripts/collect.py run \
  --max-new-per-source 50 \
  --max-total 500 \
  --generate-limit 3
```

異常終了で`generating`に残った記事は、他の生成プロセスが動いていないことを確認してから戻す。

```bash
python scripts/collect.py retry --include-generating
```
