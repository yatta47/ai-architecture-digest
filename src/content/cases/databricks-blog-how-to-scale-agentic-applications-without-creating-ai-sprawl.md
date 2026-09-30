---
type: guidance
title: AIスプロールを防ぐエンタープライズ向けエージェント共通基盤（Choice・Context・Control）
title_original: How to scale agentic applications without creating AI sprawl
company: Databricks
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- context-engineering
- multi-model-routing
- guardrails
components:
- Agent Bricks
- Omnigent
- Unity Gateway
- Unity Catalog
- Genie Ontology
- Document Intelligence
- AI Search
- Agent Memory
- Smart Routing
- Databricks Sandbox
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-scale-agentic-applications-without-creating-ai-sprawl
published_at: '2026-09-30'
---

## 概要

エージェントを多数運用する企業では、チームごとに統合やポリシーを作り込むことで、重複・不整合・コスト増といった「AIスプロール」が起きると指摘する。Databricksは、モデル・ツール・フレームワークの選択肢（Choice）、ガバナンスされた業務データと意味の共有（Context）、権限・ポリシー・評価・可観測性の一貫した管理（Control）を共通基盤として提供すべきだとし、Agent Bricks・Omnigent・Unity Gatewayによる構成を示している。

## 設計のポイント

- 業務定義やデータアクセスはUnity CatalogとGenie Ontologyによる共有コンテキスト層に集約し、エージェントごとに再構築しない。
- Omnigentでエージェントハーネスの上に共通層を置き、Unity Gatewayでモデル・ハーネス層の選択とSmart Routingを扱うことで、裏側の技術を入れ替えても周辺基盤を維持する。
- モデル・エージェント・MCPサーバー・ツールへのアクセスポリシー、ガードレール、予算・レート制限、トレースをUnity Gatewayの中央コントロールプレーンで一元管理する。
- コードやツールを実行するワークロードは、必要なデータとシステムだけに権限を絞った隔離環境（Databricks Sandbox）で動かす。

## 使いどころ

- 複数チームが別々にエージェントを開発し、統合・ポリシーの重複や不整合が目立ち始めた企業。
- 営業エージェントとサポートエージェントのように、同じ業務概念（アクティブ顧客など）を複数アプリで揃えて使いたい場面。
- 返金処理のように、依頼者より狭いタスク単位の権限でエージェントに操作を実行させたい場面。
