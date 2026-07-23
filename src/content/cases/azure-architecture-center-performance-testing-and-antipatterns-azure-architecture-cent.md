---
type: guidance
title: クラウドアプリのパフォーマンスアンチパターン集
title_original: Performance testing and antipatterns for cloud applications
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/antipatterns/
published_at: '2026-02-03'
---

## 概要

Azureの顧客事例をもとに、クラウドアプリケーションが本番の負荷にさらされた際に発生しやすい典型的なパフォーマンスアンチパターンをカタログ化した記事。Busy Database、Chatty I/O、No Cachingなど10種類のアンチパターンを挙げ、それぞれの発生原因・症状・解決の方向性を整理している。パフォーマンステストだけでは本番環境の挙動を完全には再現できないため、本番運用時の観測と是正が重要だと強調している。
