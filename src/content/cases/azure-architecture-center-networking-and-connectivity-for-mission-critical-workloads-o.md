---
type: guidance
title: ミッションクリティカルワークロード向けネットワーク・接続性設計
title_original: Networking and connectivity for mission-critical workloads
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-mission-critical/mission-critical-networking
published_at: '2026-07-10'
---

## 概要

ミッションクリティカルワークロードにおけるネットワーク・接続性の設計ガイダンス。Azure Front Doorをグローバルな入口とし、ヘルスプロービングと重み付きトラフィック分散で、独立したリージョナルなデプロイメントスタンプ間の高可用性を実現する構成を解説する。分離された仮想ネットワークやプライベートエンドポイント、WAFを用いた多層的なセキュリティ設計のトレードオフにも言及している。
