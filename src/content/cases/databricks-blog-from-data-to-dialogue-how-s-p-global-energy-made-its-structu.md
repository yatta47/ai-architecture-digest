---
type: case
title: S&P Global EnergyのGenie AgentとMCPによる対話型データ基盤
title_original: 'From data to dialogue: how S&P Global Energy made its structured data estate conversational with Databricks'
company: S&P Global Energy
industry: other
cloud:
- multi-cloud
patterns:
- text-to-sql
- data-federation
- ai-agent
- multi-agent-orchestration
components:
- Databricks Genie
- Unity Catalog
- Lakehouse Federation
- Model Context Protocol
- FastMCP
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/data-dialogue-how-sp-global-energy-made-its-structured-data-estate-conversational-databricks
published_at: '2026-09-25'
---

## 概要

S&P Global Energyは、商品・データセット群ごとにドメイン専門家がコード不要でGenie Agentを作り、それぞれを管理型MCPサーバーとして公開した。FastMCPプロキシで束ねて横断質問に対応し、Unity Catalogのガバナンスを保ったまま市場投入を月単位から日単位に短縮した。

## 設計のポイント

- データセット群ごとに小さなGenie Agentを置き、巨大な単一エージェントを避ける。
- 非DatabricksデータはLakehouse Federationで取り込まず参照し、同じガバナンスを適用する。
- FastMCPプロキシで複数のMCPサーバーを合成エンドポイントにする。

## 使いどころ

- 構造化データを顧客のエージェントへMCPで提供したいデータ提供事業者。
- 専門家主導で対話型データ製品を作りたい組織。
