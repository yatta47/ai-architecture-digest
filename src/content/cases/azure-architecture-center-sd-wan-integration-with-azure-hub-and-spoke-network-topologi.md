---
type: guidance
title: MicrosoftバックボーンとSD-WANを統合したグローバル拠点間接続の設計
title_original: SD-WAN integration with Azure hub-and-spoke network topologies - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/networking/guide/sd-wan-integration-hub-spoke-network-topologies
published_at: '2026-06-13'
---

## 概要

既存のMPLS網や専用線への投資を活かしつつ、SD-WAN機器をAzureの各リージョンのハブ仮想ネットワークにNVAとして配置し、Microsoftバックボーン上にハブ間のフルメッシュオーバーレイを構築するベンダー非依存のアーキテクチャを解説する。MPLSからインターネット接続への段階的な移行など、既存投資への影響を最小化しながら拠点間接続を最適化する方法を示す。
