---
type: guidance
title: AKS/EKSにおけるワークロードIDとクラウドリソースアクセスの比較
title_original: Kubernetes workload identity and access
ai_relevant: false
industry: cross-industry
cloud:
- azure
- aws
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/aws-professional/eks-to-aks/workload-identity
published_at: '2025-04-08'
---

## 概要

EKSのIAM Roles for Service AccountsとAKSのマネージドID/Microsoft Entra Workload IDを比較し、Kubernetesワークロードがクレデンシャルを直接管理せずにクラウドリソースへ安全にアクセスする方法を解説する。
