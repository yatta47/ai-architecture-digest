---
type: guidance
title: 複数CDN併用によるミッションクリティカルなグローバルコンテンツ配信の冗長化設計
title_original: Mission-critical global content delivery
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/networking/global-web-applications/mission-critical-content-delivery
published_at: '2026-01-27'
---

## 概要

Azure Architecture Centerは、Azure Front Doorに加えて別のCDNを併用し、単一CDN障害時にもトラフィックを自動的に切り替えるミッションクリティカルなコンテンツ配信アーキテクチャを解説する。Azure Traffic Managerの重み付けルーティングで平常時はAzure Front Doorへ全トラフィックを流し、障害時には代替CDNへフェイルオーバーする構成を示す。キャッシュフィルの遅延対策や機能差異、コスト増などのトレードオフにも言及している。
