---
type: guidance
title: Split-Brain DNSによるパブリック/社内向けWebアプリの経路分離
title_original: Use a split-brain DNS configuration to host a web app in Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/networking/split-brain-dns
published_at: '2026-05-04'
---

## 概要

同じFQDNに対し、インターネット経由のアクセスはAzure Front Door経由、社内ネットワーク経由のアクセスはExpressRoute/VPN経由とDNSで経路を出し分けるSplit-Brain DNS構成を示す。公衆網はFront DoorとApplication Gateway WAF、社内網はActive Directory DNSとオンプレミス接続を組み合わせ、QoSとセキュリティレベルを利用者の起点に応じて切り替える。
