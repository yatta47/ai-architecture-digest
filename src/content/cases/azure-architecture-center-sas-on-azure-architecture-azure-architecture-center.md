---
type: guidance
title: SASアナリティクスワークロードのAzure実行アーキテクチャ
title_original: SAS on Azure architecture
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/sas/sas-overview
published_at: '2026-05-06'
---

## 概要

SASアナリティクスをAzure上で実行するための構成を、セルフマネージドVMとAKSベースのコンテナ版の両面から解説する。API/可視化層・コンピュート層・ストレージ層（Lustre/Spectrum Scale/NFS）の3層構造と、近接配置グループやネットワークセキュリティグループによるレイテンシ低減・保護を組み合わせる。
