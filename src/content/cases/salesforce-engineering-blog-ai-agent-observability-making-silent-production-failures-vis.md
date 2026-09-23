---
type: case
title: 'Agentforce Health Monitoring: 本番エージェントの静かな可用性障害の検知'
title_original: 'AI agent observability: making silent production failures visible and actionable'
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- llmops
- ai-agent
- eval
- root-cause-analysis
components:
- Agentforce Health Monitoring
- Agentforce
- RAG Quality Monitoring
outcome:
  type: reliability
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/ai-agent-observability-making-silent-production-failures-visible-and-actionable/
published_at: '2026-09-22'
---

## 概要

SalesforceはAgentforce Health Monitoringで、リクエストが届かない、上流接続の失敗、LLMゲートウェイ障害のような、指標は正常に見えるのに応答が返らない静かな可用性障害を検知している。可用性指標と自動アラートを含む16以上の指標を備え、アラートを関連セッションの文脈につなげる。

## 設計のポイント

- エンドツーエンドの応答有無を測る可用性指標を、従来の緑のメトリクスと分けて持つ。
- セッション、推論ステップ、ツール呼び出し、エラー等のシグナルを一貫した形に揃えて評価する。
- アラートを既存の運用ワークフローへ経路付けし、セッション文脈に辿れるようにする。
- 今後はコスト、TTFT、毒性、RAG品質を追加する。

## 使いどころ

- 本番エージェントの障害を早期に検知したい運用担当者。
- ハルシネーションやコンテキスト喪失の検知を設計するチーム。
- 顧客ごとに許容基準が違うエージェント運用。
