---
type: guidance
title: Azure VPN Gatewayによるサイト間ハイブリッド接続のリファレンスアーキテクチャ
title_original: Azure VPN Gateway site-to-site connectivity for hybrid networks
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/hybrid-vpn-connectivity
published_at: '2026-08-12'
---

## 概要

オンプレミスネットワークとAzure仮想ネットワークをIPsec/IKEトンネルで接続するサイト間VPNのリファレンスアーキテクチャ。GatewaySubnetへのVPN Gatewayデプロイ、ローカルネットワークゲートウェイの作成、BGPやアクティブ-アクティブ構成による可用性向上まで、構築手順とトラフィックのランタイムフローを解説する。
