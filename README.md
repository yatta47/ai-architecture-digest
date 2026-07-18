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
