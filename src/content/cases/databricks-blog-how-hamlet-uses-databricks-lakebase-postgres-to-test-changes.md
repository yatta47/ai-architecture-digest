---
type: case
title: HamletがLakebaseのブランチでPRごとに本番データ検証を行う
title_original: How Hamlet uses Databricks Lakebase Postgres to test changes against production data
company: Hamlet
industry: public-sector
cloud:
- multi-cloud
patterns:
- ci-cd
- ai-agent
- human-in-the-loop
components:
- Databricks Lakebase
- Postgres
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-hamlet-uses-databricks-lakebase-postgres-test-changes-against-production-data
published_at: '2026-10-20'
---

## 概要

地方自治体の会議録を検索可能にするHamletは、プルリクエストごとにLakebase Postgresの本番データのブランチを作る。エンジニアとAIコーディングエージェントが本番に触れず実データでパイプラインを検証し、マージは人が承認する。

## 設計のポイント

- PR単位でデータベースをブランチし、バグの原因となった実データで本番に影響なく検証する。
- AIコーディングエージェントにブランチ上でパイプラインを実行・確認させ、最終マージは人が承認する。
- ベクトル・テキスト検索やオブジェクトストレージのブランチなど、同基盤上での拡張を検討する。

## 使いどころ

- 形式がバラバラな外部データを取り込むデータパイプラインの変更検証。
- AIコーディングエージェントを本番データ近傍で安全に動かしたいチーム。
