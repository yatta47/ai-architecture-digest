---
type: guidance
title: ミッションクリティカルWebアプリのグローバルルーティング冗長化設計
title_original: Global routing redundancy for mission-critical web applications
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/networking/global-web-applications/overview
published_at: '2026-01-08'
---

## 概要

Azure Front DoorをプライマリのグローバルルーティングとするミッションクリティカルなWebアプリケーションに対し、プラットフォーム全体の障害に備えたさらなる冗長化構成を解説する。Azure Traffic Managerの重み付けルーティングを用い、Front Door障害時に別のルーターへ手動でフェイルオーバーする二重経路のアプローチが紹介されている。ただしコスト・運用複雑性・パフォーマンスへの影響というトレードオフが大きいため、多くの場合はこの構成が不要であると強調している。
