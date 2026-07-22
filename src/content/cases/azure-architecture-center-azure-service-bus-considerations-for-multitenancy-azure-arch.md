---
type: guidance
title: Azure Service Busにおけるマルチテナント分離モデルの選択指針
title_original: Azure Service Bus considerations for multitenancy
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/service-bus
published_at: '2026-05-25'
---

## 概要

マルチテナントシステムでAzure Service Busを使う際の分離モデル（テナント専用ネームスペース、共有ネームスペース内の専用トピック/キュー、完全共有）を比較し、データ分離・パフォーマンス分離・運用複雑性のトレードオフを整理した記事。
