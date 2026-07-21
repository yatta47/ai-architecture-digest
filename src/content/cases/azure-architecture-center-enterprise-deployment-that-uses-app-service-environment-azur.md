---
type: guidance
title: App Service Environmentを使ったセキュアなエンタープライズWebアプリのリファレンス構成
title_original: Enterprise deployment that uses App Service Environment
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/web-apps/app-service-environment/architectures/app-service-environment-standard-deployment
published_at: '2026-07-02'
---

## 概要

Azure App Service Environment(ASEv3)を用いた一般的なエンタープライズWebワークロードのリファレンスアーキテクチャと、セキュリティを強化するためのベストプラクティスを紹介する記事。Application GatewayのWAFでインターネット入口を保護し、内部ロードバランサー型のASEをVNet内の専用サブネットに隔離、Azure Firewallでアウトバウンドを制御し、Service Bus・Cosmos DB・SQL Database・Key VaultへはプライベートエンドポイントとマネージドIDで接続する構成を示している。
