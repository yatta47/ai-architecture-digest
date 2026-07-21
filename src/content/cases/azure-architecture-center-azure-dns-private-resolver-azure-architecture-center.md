---
type: guidance
title: Azure DNS Private Resolverでオンプレミスとのハイブリッド名前解決をDNSフォワーダVMなしに簡素化する
title_original: Azure DNS Private Resolver
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/networking/architecture/azure-dns-private-resolver
published_at: '2026-06-18'
---

## 概要

従来はDNSフォワーダVMを介して行っていたオンプレミスとAzure間の再帰的DNS名前解決を、Azure DNS Private Resolverによって専用VMなしに実現する構成を解説する。ハブスポーク型ネットワークのハブにインバウンド・アウトバウンドエンドポイントを配置し、Azure ExpressRouteやAzure Firewallと組み合わせることで、オンプレミスからAzureプライベートDNSへ、またその逆方向への名前解決を安全に行える。
