---
type: announcement
title: Claude PlatformのOpenTelemetryをDatabricks MLflowへ
title_original: Claude Platform now supports native OpenTelemetry observability in Databricks MLflow
company: Databricks
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
components:
- Databricks MLflow
- Unity Catalog
- Zerobus Ingest
- Claude Managed Agents
- OpenTelemetry
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/claude-platform-now-supports-native-opentelemetry-observability-databricks-mlflow
published_at: '2026-11-03'
---

## 概要

Claude Platform（Anthropic SDK、Messages API、Managed Agents）のネイティブOpenTelemetryトレースをDatabricks MLflowに送れるようになった（Public Beta）。Zerobus Ingest経由でUnity Catalogに保存し、トレース分析とMLflow Issuesで失敗調査と評価ができる。

## 設計のポイント

- OTel標準でスパンを出力し、他サービスのトレースと同じ道具で扱う。
- Unity Catalogでトレースのアクセスを管理し、SQLで検索できる。
- 専門家レビューと同じテストケースで改善を評価する。

## 使いどころ

- Claudベースのエージェントを既存のDatabricks基盤で監視・評価したいとき。
