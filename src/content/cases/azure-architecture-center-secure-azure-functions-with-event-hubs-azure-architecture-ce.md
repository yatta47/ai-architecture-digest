---
type: guidance
title: Azure Functions と Event Hubs 連携のセキュリティ設計ガイド
title_original: Secure Azure Functions with Azure Event Hubs
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/serverless/event-hubs-functions/security
published_at: '2026-07-08'
---

## 概要

Azure Functions から Azure Event Hubs へアクセスする際の認可方式として、Microsoft Entra ID(Azure RBAC)と共有アクセス署名(SAS)の使い分け、およびマネージドIDによるID連携を解説する。あわせてIPファイアウォール規則・サービスエンドポイント・プライベートエンドポイントによるネットワーク制限や、vnetRouteAllEnabled有効時の全トラフィック制御など、最小権限原則に基づく防御設計の考慮点をまとめている。
