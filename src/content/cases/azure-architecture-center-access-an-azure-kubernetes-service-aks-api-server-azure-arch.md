---
type: guidance
title: AKS APIサーバーへの安全なアクセス方式ガイド
title_original: Access an Azure Kubernetes Service (AKS) API server
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/security/access-azure-kubernetes-service-cluster-api-server
published_at: '2026-04-30'
---

## 概要

パブリック/プライベートAKSクラスターのAPIサーバーへ安全に接続する方法を整理したガイド。Microsoft Entra IDとAzure RBACによるアクセス制御、許可IPレンジ制限、DDoS Protectionに加え、プライベートクラスターへはジャンプボックスやAzure Bastion、VPN、ExpressRoute、`az aks command invoke`など複数の接続手段の使い分けを解説する。
