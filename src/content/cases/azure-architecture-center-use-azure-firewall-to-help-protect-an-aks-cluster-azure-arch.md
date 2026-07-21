---
type: guidance
title: Azure Firewallで保護するプライベートAKSクラスターのハブスポーク構成
title_original: Use Azure Firewall to help protect an AKS cluster
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/aks/aks-firewall
published_at: '2026-06-23'
---

## 概要

Terraform と Azure DevOps を使い、ハブスポーク型ネットワークにプライベートAKSクラスターを構築するリファレンスアーキテクチャ。Azure Firewallがクラスターとの間の入出力トラフィックをDNAT/ネットワーク/アプリケーションルールとSNAT、脅威インテリジェンスベースのフィルタリングで検査・保護し、Azure Bastion経由のジャンプボックスやAzure Private Link経由のKey Vault/Container Registryアクセスと組み合わせて全体のセキュリティを高めている。
