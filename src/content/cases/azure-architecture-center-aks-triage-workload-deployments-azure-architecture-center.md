---
type: guidance
title: AKSワークロードのデプロイ監視ガイド
title_original: Monitor workload deployments
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/operator-guides/aks/aks-triage-deployment
published_at: '2025-01-20'
---

## 概要

Azure Kubernetes Service (AKS) でDeployment/DaemonSet/ReplicaSetのレプリカ状態やサービス・ストレージの健全性を、Azureポータル、Container Insights、kubectl、Prometheus/Grafanaなど複数のツールで監視する方法を解説する。AKS運用者が本番クラスタの状態を継続的に把握するための実務ガイド。
