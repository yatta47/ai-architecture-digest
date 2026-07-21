---
type: guidance
title: AKSからAzure Container Appsへのマイクロサービス・リプラットフォーム構成
title_original: Deploy Microservices to Azure Container Apps
ai_relevant: false
industry: logistics
cloud:
- azure
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/serverless/microservices-with-container-apps
published_at: '2026-07-01'
---

## 概要

Kubernetes(AKS)向けに構築済みのドローン配送マイクロサービスを、アプリケーションコードを変更せずにAzure Container Appsへリプラットフォームするリファレンスアーキテクチャ。Ingestion/Workflow/Package/Drone Scheduler/Deliveryの各コンテナアプリをAzure Service Busで疎結合に連携させ、既存のContainer RegistryやKey Vaultを再利用しつつ、KEDAベースのオートスケールや統合ログ監視などContainer Appsの標準機能でKubernetes運用の複雑さを削減する例を示す。
