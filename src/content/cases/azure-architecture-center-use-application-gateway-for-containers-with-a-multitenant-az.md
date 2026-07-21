---
type: guidance
title: 'マルチテナントAKS向け共有Ingress: Application Gateway for Containers構成'
title_original: Use Application Gateway for Containers with a multitenant Azure Kubernetes Service cluster
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/aks-agic/aks-agc
published_at: '2026-06-30'
---

## 概要

Azureのマルチテナント AKS クラスタで、単一のApplication Gateway for Containersインスタンスを共有Ingressとして使う参照アーキテクチャ。各テナントは独自のnamespace・Kubernetes Gateway・HTTPRoute・TLS証明書を持ち、プラットフォームチームがApplication Gateway自体を一元所有・管理する。WAFポリシー(DRS 2.1)による防御と、Azure Bastion経由のプライベートAKS API管理アクセスを組み合わせている。
