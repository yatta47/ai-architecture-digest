---
type: guidance
title: Azure Firewallで構成する境界ネットワーク(DMZ)付きハイブリッドネットワーク
title_original: Implement a secure hybrid network
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/dmz/secure-vnet-dmz
published_at: '2026-07-03'
---

## 概要

オンプレミスネットワークをAzureに拡張する際、全ての受信・送信トラフィックをAzure Firewallに通す境界ネットワーク(DMZ)を構成するリファレンスアーキテクチャ。DNAT/SNATの挙動やRBACによる権限分離など、ハイブリッド環境の監査・セキュリティ要件に対応する設計を示す。
