---
type: guidance
title: Azure Virtual WANによるマネージド型ハブ&スポークネットワークトポロジ
title_original: Hub-spoke network topology that uses Azure Virtual WAN
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/networking/architecture/hub-spoke-virtual-wan-architecture
published_at: '2026-05-27'
---

## 概要

自己管理型ハブ&スポークの代替として、Microsoft管理のAzure Virtual WANでハブ間ピアリングとルーティングを一元化するネットワークアーキテクチャ。Azure Firewallと統合したセキュアハブにより、運用オーバーヘッドを削減しつつ全トラフィックのファイアウォール検査を徹底する。
