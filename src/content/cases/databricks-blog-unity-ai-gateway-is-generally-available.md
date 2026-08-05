---
type: announcement
title: エージェント・モデル・MCP横断でAI支出とガードレールを一元統制するUnity AI Gateway
title_original: Unity AI Gateway is Generally Available
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- llm-gateway
- cost-optimization
- guardrails
- multi-model-routing
components:
- Unity AI Gateway
- Unity Catalog
- Databricks Genie
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/unity-ai-gateway-generally-available
published_at: '2026-08-04'
---

## 概要

DatabricksがUnity AI GatewayをGA公開。エージェント・モデル・MCP・スキル・ツールを横断してAI支出の可視化とハードスペンドキャップ、品質/コスト/予算に基づく動的ルーティング、ランタイムガードレールを一元的な制御プレーンで提供する。Rivian、Zepto、STRABAGなど既存顧客の事例も紹介されている。

## 設計のポイント

- Unity CatalogにAIとデータのガバナンスを統合し、エージェント・モデル・MCP・スキル横断で単一の制御プレーンとする
- 品質・コスト・パフォーマンス・予算に基づき各リクエストを最適なモデルへ動的にルーティングするSmart Routingで高価なモデルを本当に必要なタスクに絞る
- ハードスペンドキャップとユーザー/グループ単位の予算設定で暴走コストをリアルタイムに止める
- ランタイムガードレールとコンテキストに応じたポリシーでPIIや機密データの漏えいを防ぎつつ開発者のモデル選択の自由度を保つ

## 使いどころ

- 何千ものカスタムエージェントとツールが乱立し、AI支出の可視化ができていない大企業
- 複数のモデルプロバイダーを併用しつつベンダーロックインを避けたい組織
- エージェントが機密データにアクセスする際のセキュリティ・監査要件を満たしたい規制業界
