---
type: guidance
title: Azure Local上で動くAKSのベースラインアーキテクチャ
title_original: Azure Kubernetes Service (AKS) Baseline Architecture for AKS on Azure Local
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/hybrid/aks-baseline
published_at: '2026-05-30'
---

## 概要

Azure Arcリソースブリッジを制御面として、オンプレのAzure Local基盤上に最大32クラスタのAKSをホストするベースライン構成。ネットワーク・セキュリティ・監視の設計指針と、Azure Policy/Defender for Cloudによるハイブリッドガバナンスを示す。
