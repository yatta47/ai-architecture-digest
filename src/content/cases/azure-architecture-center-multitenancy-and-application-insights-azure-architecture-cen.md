---
type: guidance
title: マルチテナントAzureアプリケーションにおけるApplication Insightsのテナント分離モデル選定
title_original: Multitenancy and Application Insights
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/application-insights
published_at: '2025-08-29'
---

## 概要

Azure Architecture Centerの本記事は、マルチテナントシステムでApplication Insightsを利用する際のテナンシーモデルを整理したガイダンスである。グローバル共有インスタンス、スタンプ単位のインスタンス、テナント単位の専用インスタンスという3つの分離モデルについて、データ分離・性能分離・デプロイ複雑性・運用複雑性の観点でトレードオフを比較している。テナント数やデータ機密性への要求に応じて適切なモデルを選ぶための判断材料を提供している。
