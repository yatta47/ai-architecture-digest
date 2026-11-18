---
type: announcement
title: Unity Gateway Insights：エージェントトレース分析でトークンの無駄を可視化
title_original: Introducing Unity Gateway Insights
company: Databricks
industry: cross-industry
cloud: []
patterns:
- llmops
- llm-gateway
- multi-model-routing
- cost-optimization
components:
- Unity Gateway
- Genie
- MCP
- Smart Routing
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/introducing-unity-gateway-insights
published_at: '2026-11-18'
---

## 概要

Databricksは、Unity Gatewayを流れる大量のエージェントトレースをGenieで分析し、MCPエラー、軽い処理への高価なモデル使用、共通化すべき反復ワークフローを報告するInsightsを発表した。社内ではMCPの7つの不具合修正で年約120万ドルの削減が見込まれた。

## 設計のポイント

- ゲートウェイでトレースを集約し、ビジネスデータと突き合わせて分析する。
- MCPエラーの再試行など成功に見えるが無駄な消費を検出する。
- タスク複雑度で安価なモデルへルーティングし、反復作業はスキル化する。

## 使いどころ

- コーディングエージェントを全社展開し、トークンコストを管理する組織。
- MCPサーバーの品質改善の優先度を決めたいプラットフォーム担当。
