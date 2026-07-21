---
type: guidance
title: Azure VMベースラインの多層Webアプリ基盤アーキテクチャ
title_original: Azure Virtual Machines baseline architecture
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/virtual-machines/baseline
published_at: '2026-06-03'
---

## 概要

インターネット向けマルチティアWebアプリケーションをAzure Virtual Machine Scale Sets上に構築するための基盤リファレンスアーキテクチャ。Application GatewayによるWAF付き負荷分散、Bastionによる安全な運用アクセス、Key Vaultでの証明書管理など、コンピューティング・ネットワーク・監視の各コンポーネントの構成方針をまとめている。
