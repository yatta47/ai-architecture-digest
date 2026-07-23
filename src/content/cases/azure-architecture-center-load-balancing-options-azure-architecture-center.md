---
type: guidance
title: Azureの負荷分散サービス選定ガイド
title_original: Load balancing options
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview
published_at: '2025-11-12'
---

## 概要

Azureには API Management、Application Gateway、Azure Front Door、Load Balancer、Traffic Manager という複数の負荷分散サービスが存在し、それぞれグローバル/リージョナルの範囲やHTTP(S)対応可否が異なる。本記事はトラフィック種別・グローバル/リージョナルの要件・可用性(SLA)・コストという観点から、ワークロードに適したサービスを選定するための考慮事項を整理している。
