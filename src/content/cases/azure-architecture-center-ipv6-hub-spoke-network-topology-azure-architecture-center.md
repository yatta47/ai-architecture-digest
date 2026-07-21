---
type: guidance
title: ハブスポーク型ネットワークをIPv6デュアルスタックに移行するアーキテクチャ
title_original: IPv6 hub-spoke network topology
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/networking/guide/ipv6-architecture
published_at: '2026-06-03'
---

## 概要

既存のIPv4ハブスポーク型ネットワークをIPv4/IPv6デュアルスタック構成へ段階移行する参照アーキテクチャ。Azure Firewall・VPN Gateway・ExpressRoute・Load BalancerをデュアルスタックにしIPv6用UDRで経路制御を行い、Virtual Network ManagerとAzure Monitorでハブ・スポーク全体の管理と可観測性を確保する。
