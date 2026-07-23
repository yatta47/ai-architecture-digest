---
type: guidance
title: IaaSからPaaSへ:運用負荷を減らすAzureサービス選定ガイド
title_original: Use platform as a service (PaaS) options
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/managed-services
published_at: '2025-12-03'
---

## 概要

IaaSとPaaSの違いを整理し、インフラの構築・保守を自前で行うIaaSに対し、PaaSはプラットフォームの運用管理をクラウド側が担う点を解説する。自前運用のRabbitMQをAzure Service Busに置き換える例のように、要件がIaaSの自由度を必須としない場合はPaaSの活用を推奨し、Active DirectoryやElasticsearch、Redis、SQL Serverなど代表的な自己運用技術に対応するAzure PaaSサービス(Microsoft Entra ID、Azure AI Search、Azure Managed Redis、Azure SQL Databaseなど)の対応表を示す。
