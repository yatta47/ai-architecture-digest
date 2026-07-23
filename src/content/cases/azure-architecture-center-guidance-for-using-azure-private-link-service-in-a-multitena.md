---
type: guidance
title: Azureマルチテナントソリューションにおけるプライベートリンク活用
title_original: Guidance for using Azure Private Link in a multitenant solution
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/private-link
published_at: '2025-12-16'
---

## 概要

マルチテナントSaaSソリューションでAzure Private Linkを使ってテナントごとのプライベート接続を提供する際の設計上の考慮点を解説する記事。重複するIPアドレス空間の扱い、プライベートエンドポイントのプロビジョニング手順、サービスごとの上限、パブリック接続との併用パターンなどを取り上げている。
