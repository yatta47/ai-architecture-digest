---
type: guidance
title: Azure Event Hubsのマルチテナント分離モデル設計ガイド
title_original: Multitenancy and Azure Event Hubs
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/event-hubs
published_at: '2026-07-07'
---

## 概要

Azure Event Hubsをマルチテナント基盤で使う際の3つの分離モデル(専用namespace、共有namespace+専用event hub、完全共有)をデータ分離・性能分離・運用コストの観点で比較し、アプリケーショングループやパーティションの使い方など実装上の注意点をまとめたガイド。
