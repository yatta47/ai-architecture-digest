---
type: guidance
title: マルチテナント環境のNoisy Neighbor（うるさい隣人）問題への対処
title_original: Noisy Neighbor antipattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/antipatterns/noisy-neighbor/noisy-neighbor
published_at: '2026-03-07'
---

## 概要

共有リソースを使うマルチテナントシステムで、一部テナントの過剰利用が他テナントの性能を劣化させるNoisy Neighborアンチパターンを解説。スロットリング・予約容量・リソースガバナンスによる緩和策をクライアント側／プロバイダー側の両方から整理する。
