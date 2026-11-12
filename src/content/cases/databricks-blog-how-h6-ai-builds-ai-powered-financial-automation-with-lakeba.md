---
type: case
title: H6.aiの会計処理自動化：顧客別Lakebaseとブランチで実データ回帰テスト
title_original: How H6.ai builds AI-powered financial automation with Lakebase Postgres
company: H6.ai
industry: financial-services
cloud: []
patterns:
- llmops
- eval
- multi-tenant-analytics
- document-processing
components:
- Databricks Lakebase
- Postgres
- ERP
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-h6ai-builds-ai-powered-financial-automation-lakebase-postgres
published_at: '2026-11-12'
---

## 概要

H6.aiは買掛金処理の自動化基盤で、顧客ごとに専用のLakebase Postgresを持たせてデータを分離している。コピーオンライトのブランチで請求書問題の時点の状態を再現し、AI判定パネルと組み合わせて本番前にモデルやエンジン変更を実データで検証する。

## 設計のポイント

- 顧客ごとに専用DBを割り当て、金融データの分離を担保する。
- コピーオンライトのブランチで問題時点の状態を丸ごと保存し、モックなしで再現する。
- 使い捨てブランチでモデル変更を実ケースに対し検証し、AI審査員で採点する。

## 使いどころ

- データが刻々と変わり回帰テストが難しい業務AI。
- 顧客別のデータ分離が必須のマルチテナント基盤。
- 障害ケースを本番に触れず再現したい運用チーム。
