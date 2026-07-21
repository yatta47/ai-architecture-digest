---
type: guidance
title: マルチリージョン構成のAKSベースラインアーキテクチャ
title_original: AKS baseline for multiregion clusters
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-multi-region/aks-multi-cluster
published_at: '2026-06-11'
---

## 概要

複数のAzureリージョンでAKSクラスターをアクティブ/アクティブ構成で運用するマルチリージョンのリファレンスアーキテクチャ。Azure Front Doorによるグローバルなレイヤー7ルーティング、Azure Kubernetes Fleet Managerによるクラスタ横断のバージョン管理、Azure Container Registryのジオレプリケーションを組み合わせ、GeodeパターンとDeployment Stampsパターンによって高可用性と障害耐性を実現する。各リージョンはハブ&スポーク構成とAvailability Zoneをまたいだノード配置により、リージョン障害やゾーン障害に備える。
