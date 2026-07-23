---
type: guidance
title: スポットVM前提でのオーケストレーション設計とコスト最適化
title_original: Build workloads on spot virtual machines
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/spot/spot-eviction
published_at: '2026-03-06'
---

## 概要

最大90%安価だが強制退避されうるAzureスポットVMを、バッチ処理など中断耐性のあるワークロードに適用するための設計ガイド。退避タイプ・退避ポリシーの選び方と、柔軟なオーケストレーションによる耐障害設計を解説する。
