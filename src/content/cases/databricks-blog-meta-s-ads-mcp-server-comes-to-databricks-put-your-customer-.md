---
type: announcement
title: Meta広告MCPサーバーをDatabricks Genieに接続
title_original: Meta's Ads MCP Server Comes to Databricks
company: Databricks
industry: media
cloud:
- multi-cloud
patterns:
- ai-agent
- guardrails
- text-to-sql
components:
- Databricks Genie
- Meta ads MCP server
- Databricks Marketplace
- Unity Catalog
- Unity Gateway
- Model Context Protocol
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/meta-ads-mcp-databricks
published_at: '2026-10-06'
---

## 概要

Metaの広告MCPサーバー（25以上のツール）がDatabricks Marketplaceで利用可能になり、Genieから自然言語でキャンペーン実績を社内の統制済みデータと合わせて分析・運用できる。接続はUnity Catalogで管理し、ツール呼び出しはUnity Gatewayが統制・監査する。

## 設計のポイント

- 外部SaaSをMCPサーバーとして接続し、社内データと同じ対話で扱えるようにする。
- 接続アクセスをUnity Catalogで、ツール呼び出しをゲートウェイで統制し監査ログを残す。
- チャーンスコア等の社内指標を広告予算判断に直接使う。

## 使いどころ

- データ・広告運用チームがCSVや手作業連携なしに施策へ反映したい場面。
- エージェントが本番広告アカウントを操作する際の統制設計。
