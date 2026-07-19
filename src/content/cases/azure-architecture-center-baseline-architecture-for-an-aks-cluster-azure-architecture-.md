---
type: guidance
title: AKSクラスターの本番運用に向けたベースラインリファレンスアーキテクチャ
title_original: Baseline architecture for an Azure Kubernetes Service (AKS) cluster
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks/baseline-aks
published_at: '2026-07-09'
---

## 概要

Azure Kubernetes Service (AKS) クラスターを本番運用する際の最小限の推奨ベースライン構成を示すリファレンスアーキテクチャ。ハブスポーク型ネットワークにAzure Firewall、Bastion、Application Gatewayを配置し、Microsoft Entra ID統合やAzure Monitorによる可観測性、可用性ゾーンを用いた事業継続性を確保する。ネットワーキング・セキュリティ・アイデンティティなど複数チームが協調してAKS基盤を構築する際の出発点として設計されている。
