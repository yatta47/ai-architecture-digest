---
type: guidance
title: App Service Environmentのゾーン冗長構成による高可用性エンタープライズ配置
title_original: High availability enterprise deployment that uses App Service Environment
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/web-apps/app-service-environment/architectures/app-service-environment-high-availability-deployment
published_at: '2026-07-02'
---

## 概要

App Service Environment v3をゾーン冗長構成でデプロイし、可用性ゾーン単位の障害の影響を受けにくいエンタープライズ向け高可用性アーキテクチャを解説する。Application Gateway v2やAzure Firewall、Azure Managed Redisなどもゾーン冗長対応のコンポーネントとして組み合わせ、単一リージョン内でWebアプリ・API・関数の可用性を高める設計を示す。
