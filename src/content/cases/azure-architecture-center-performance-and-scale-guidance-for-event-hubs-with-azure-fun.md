---
type: guidance
title: Event HubsとAzure Functionsによるイベント処理のパフォーマンス・スケーリング設計
title_original: Performance and scale guidance for Event Hubs and Azure Functions
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/serverless/event-hubs-functions/performance-scale
published_at: '2026-07-08'
---

## 概要

Azure Event HubsとAzure Functionsを組み合わせたイベント処理システムのパフォーマンスとスケーラビリティを最適化するためのガイダンス。関数を専用の関数アプリ・ストレージアカウント・コンシューマーグループに分離することでリソース競合を避け、Flex ConsumptionなどのホスティングプランやスループットユニットなどEvent Hubsのスケーリング設定を適切に選ぶことを推奨している。
