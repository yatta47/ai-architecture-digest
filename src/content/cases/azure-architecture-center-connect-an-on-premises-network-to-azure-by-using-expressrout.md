---
type: guidance
title: ExpressRouteとVPNフェイルオーバーによるオンプレミス-Azure間接続のリファレンスアーキテクチャ
title_original: Connect an on-premises network to Azure by using ExpressRoute with VPN failover
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/expressroute-vpn-failover
published_at: '2026-05-23'
---

## 概要

オンプレミスネットワークとAzure仮想ネットワークをExpressRouteで接続し、サイト間VPNをフェイルオーバー経路として構成するリファレンスアーキテクチャ。ExpressRoute障害時はプライベートピアリングのトラフィックのみIPsec VPNへ切り替わり、Microsoftピアリングはインターネット経由になる制約を説明している。
