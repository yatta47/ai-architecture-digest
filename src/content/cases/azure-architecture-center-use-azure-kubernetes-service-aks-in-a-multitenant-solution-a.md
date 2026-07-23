---
type: guidance
title: AKSでマルチテナント基盤を構築するための分離設計ガイド
title_original: Use Azure Kubernetes Service (AKS) in a multitenant solution
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/aks
published_at: '2026-01-22'
---

## 概要

Azure Kubernetes Service (AKS)を複数テナントで共有する際の設計ガイド。社内複数チームによる共有とSaaS事業者による顧客ごとのインスタンス共有という2つの利用形態、信頼度に応じたソフト/ハードマルチテナンシーの違い、クラスタ・namespace・ノードプール・Pod・コンテナという分離レイヤーの選択肢を整理し、namespaceとRBACによるコントロールプレーン分離を基本方針として推奨している。
