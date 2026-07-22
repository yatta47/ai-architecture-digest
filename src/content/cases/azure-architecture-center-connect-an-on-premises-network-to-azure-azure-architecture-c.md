---
type: guidance
title: オンプレミスネットワークとAzureの接続方式比較（VPN/ExpressRoute）
title_original: Connect an on-premises network to Azure
ai_relevant: false
industry: cross-industry
cloud:
- azure
- on-prem
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/
published_at: '2026-05-06'
---

## 概要

オンプレミスとAzure仮想ネットワークを接続する複数の方式（VPN Gateway、ExpressRoute、両者の併用）を比較し、それぞれの帯域・可用性SLA・構成の複雑さのトレードオフを示す。ワークロードのトラフィック量や求める可用性に応じた接続方式選定の指針を提供する。
