---
type: announcement
title: Genieが Microsoft Teams・Copilot Cowork・Excelでガバナンス付き回答を提供
title_original: What's new for Genie in Microsoft Copilot Cowork and chat, Microsoft Teams and Excel
company: Databricks
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- context-engineering
- guardrails
components:
- Genie
- Genie Ontology
- Unity Catalog
- Unity Gateway
- Microsoft Teams
- Microsoft Copilot Studio
- Excel
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/whats-new-genie-microsoft-copilot-cowork-and-chat-microsoft-teams-and-excel
published_at: '2026-11-18'
---

## 概要

Databricks GenieがMicrosoft Teams（一般提供）、Copilot Cowork、Excel、Copilot Studioから利用可能になった。Genie Ontologyによる業務文脈とUnity Catalog/Gatewayによる権限・予算・ツール制御を維持したまま、既存の業務ツール内で回答を得られる。

## 設計のポイント

- 業務セマンティクスをOntologyに統合して回答の根拠を揃える。
- Unity Catalogでユーザー単位のデータ権限を強制する。
- 既存のMicrosoft UIにプラグインで接続し、導入摩擦を下げる。

## 使いどころ

- Teamsのチャンネル上で営業データを問い合わせたい営業マネージャー。
- AIアシスタント導入時にガバナンスを維持したいデータ管理者。
