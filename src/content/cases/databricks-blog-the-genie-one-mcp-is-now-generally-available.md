---
type: announcement
title: Genie One MCPが一般提供開始、Unity Gateway経由で統治された文脈を全エージェントへ
title_original: The Genie One MCP is now generally available
company: GetYourGuide
industry: cross-industry
cloud:
- multi-cloud
patterns:
- context-engineering
- llm-gateway
- data-federation
components:
- Genie One MCP
- Unity Gateway
- Genie Ontology
- Claude Cowork
- ChatGPT
- Cursor
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/genie-one-mcp-now-generally-available
published_at: '2026-09-22'
---

## 概要

Genie One MCPサーバーが全Databricksユーザーに一般提供された。Unity Gateway上のマネージドMCPサービスとして稼働し、集中的なガバナンス・きめ細かいポリシー・監査ログを備えつつ、構造化・非構造化データにまたがるGenie Oneの回答をどのエージェントクライアントからも一貫して取得できるようにする。

## 設計のポイント

- Genie One MCPをUnity Gateway配下のマネージドサービスとして提供し監査ログとポリシーを一元化した
- 単一のガバナンスされた入口を置くことでエージェントごとのフォーマット別コネクタ乱立（agent sprawl）を防いだ
- 複雑なサブタスクはドメイン別のGenie Agentに動的委譲するインテリジェントルーティングを備える
- MCP Appにより対応クライアント上でインタラクティブな可視化とGenie Ontologyの出典引用をリアルタイム表示できる

## 使いどころ

- 資料作成エージェントに信頼できる実績数値を組み込みたい業務部門
- 顧客の利用状況低下を検知してアウトリーチするエージェントに根拠データを渡したいカスタマーサクセスチーム
- コーディングエージェントに現行のビジネス定義を踏まえた変更をさせたい開発チーム
