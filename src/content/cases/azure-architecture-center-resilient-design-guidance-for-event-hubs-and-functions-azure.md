---
type: guidance
title: Azure Event Hubs×Functionsをレジリエントに設計する(冪等性・重複排除・パーティション設計)
title_original: Resilient Azure Event Hubs and Azure Functions design
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/serverless/event-hubs-functions/resilient-design
published_at: '2026-07-07'
---

## 概要

Event Hubsでトリガーされる Azure Functions を大量データに耐える形で設計するためのガイド。At-least-once配信を前提にした冪等な処理の実装、チェックポイントに起因する重複イベントへの対処、デッドレター機構が標準搭載されていない点への回避策などをまとめている。
