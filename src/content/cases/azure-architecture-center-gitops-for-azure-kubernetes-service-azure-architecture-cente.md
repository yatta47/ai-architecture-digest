---
type: guidance
title: AKSにおけるGitOps運用パターン（Flux/Argo CD）
title_original: GitOps for Azure Kubernetes Service
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/gitops-aks/gitops-blueprint-aks
published_at: '2025-11-03'
---

## 概要

AKSクラスタの構成管理にFluxやArgo CDを使ったGitOpsパターンを解説。プル型の継続的なリコンシリエーションにより、Git上の望ましい状態とクラスタの実状態を同期させる複数のシナリオを紹介している。
