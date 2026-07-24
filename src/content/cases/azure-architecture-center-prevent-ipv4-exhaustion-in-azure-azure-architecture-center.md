---
type: guidance
title: AzureにおけるIPv4アドレス枯渇を防ぐネットワーク設計
title_original: Prevent IPv4 exhaustion in Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/networking/guide/internet-protocol-version-4-exhaustion
published_at: '2025-06-17'
---

## 概要

Azureのランディングゾーン環境でIPv4アドレス空間を効率的に使うための2つの手法（サブネットピアリングによる非経路対象サブネットの除外、Private Link経由の分離仮想ネットワーク）を解説する。マイクロサービス化やコンテナ化で加速するIPv4消費への対策を示す。
