---
type: guidance
title: AKSノードとKubernetesバージョンのパッチ・アップグレード運用
title_original: Patch and upgrade Azure Kubernetes Service worker nodes and Kubernetes versions
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/operator-guides/aks/aks-upgrade-practices
published_at: '2026-03-06'
---

## 概要

AKSのノードOSパッチ・ノードイメージ更新・四半期のKubernetesバージョンアップグレードを安全に行うための運用ガイド。PodDisruptionBudgetの設定やmaintenance window、undrainableノードの扱いなど、アップグレード時の可用性低下を防ぐベストプラクティスをまとめる。
