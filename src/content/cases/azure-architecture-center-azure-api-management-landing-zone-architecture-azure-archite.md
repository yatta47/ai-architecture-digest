---
type: guidance
title: Application Gateway背後で内部/外部APIを一元管理するAPI Managementランディングゾーン構成
title_original: Azure API Management landing zone architecture
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/integration/app-gateway-internal-api-management-function
published_at: '2026-05-27'
---

## 概要

Azure Application GatewayをAPI Managementの前段に置き、内部APIと外部APIを単一のAPI Managementインスタンスで統合管理しつつ、公開APIを常にゲートウェイの背後に隠すランディングゾーンアーキテクチャ。WAFポリシーとプライベートエンドポイントで攻撃対象領域を絞り込む。
