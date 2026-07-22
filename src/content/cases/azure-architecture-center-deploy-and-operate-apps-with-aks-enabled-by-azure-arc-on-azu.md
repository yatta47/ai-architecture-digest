---
type: guidance
title: Azure Arc対応AKSでのGitOpsアプリ配信パイプライン
title_original: Deploy and operate apps with AKS enabled by Azure Arc on Azure Local
ai_relevant: false
industry: cross-industry
cloud:
- azure
- on-prem
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/hybrid/aks-hybrid-azure-local
published_at: '2026-05-08'
---

## 概要

Azure Local上のAKS on Azure Arcクラスターに対し、Flux/GitOpsを使ってコンテナアプリをデプロイ・運用するリファレンス構成を解説する。Gitリポジトリへの構成プッシュをFluxが検知し、ローリング更新でクラスタに反映することで最小ダウンタイムを実現する。Azure PipelinesによるCI/CDとコンテナレジストリ連携も含む。
