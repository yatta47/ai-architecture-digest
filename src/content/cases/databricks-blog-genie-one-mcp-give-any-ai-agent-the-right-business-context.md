---
type: guidance
title: Genie OntologyでガバナンスされたビジネスコンテキストをMCP経由で全エージェントに供給
title_original: 'Genie One MCP: How to give any AI Agent the Right Business Context'
industry: cross-industry
cloud:
- multi-cloud
patterns:
- context-engineering
- data-federation
- llm-gateway
components:
- Genie One
- Genie Ontology
- MCP
- ChatGPT
- Claude
- Microsoft Copilot
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/genie-one-mcp-give-any-ai-agent-right-business-context
published_at: '2026-09-22'
---

## 概要

汎用AIエージェントはデータへのアクセスはできても、どの定義・出典が正しいかというビジネス文脈を欠くため信頼できる回答を返せない。Genie OneはGenie Ontologyに承認済みの指標定義・データ関係・出典の権威・権限を一度だけ定義し、Genie One MCP経由でChatGPTやClaude、Microsoft Copilotなど任意のMCP対応エージェントに同じガバナンスされた文脈を提供する。

## 設計のポイント

- 承認済み指標定義・データ関係・出典の権威・アクセス権限をGenie Ontologyという単一の文脈層に集約した
- スキーマへの直接アクセスではなく文脈層を経由させることで承認済みのJOINや定義をエージェントに推測させない設計にした
- MCPサーバーとして公開することでクライアント（ChatGPT/Claude/Copilot/コーディングエージェント）を問わず同じ権限制御と回答一貫性を確保した
- 生スキーマを都度読み込ませる方式に比べトークン消費とレイテンシを抑えられる

## 使いどころ

- 複数のAIアシスタントを併用していて指標の定義がツールごとに食い違う組織
- マーケティング・財務・カスタマーサクセスなど業務部門がそれぞれ異なるAIツールで同じデータを参照するケース
- コーディングエージェントに承認済みのビジネス定義を踏まえた変更をさせたい開発チーム
