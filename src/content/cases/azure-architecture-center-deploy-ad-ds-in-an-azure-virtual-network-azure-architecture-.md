---
type: guidance
title: オンプレミスADをAzure仮想ネットワークへ拡張するハイブリッド認証アーキテクチャ
title_original: Deploy AD DS in an Azure virtual network
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/identity/adds-extend-domain
published_at: '2026-06-17'
---

## 概要

オンプレミスのActive Directoryドメインサービス(AD DS)をAzure仮想ネットワークに拡張し、クラウド側でも認証をローカルに処理できるようにするリファレンスアーキテクチャ。VPN GatewayまたはExpressRouteで双方向レプリケーションを行い、AD DSは専用サブネットとNSGで保護する。可用性ゾーンに分散した最低2台のドメインコントローラと静的IP、永続ディスクの利用を推奨する。
