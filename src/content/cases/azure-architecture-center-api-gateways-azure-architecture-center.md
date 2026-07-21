---
type: guidance
title: マイクロサービスにおけるAPIゲートウェイ活用ガイド
title_original: Use API gateways in microservices
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/microservices/design/gateway
published_at: '2026-06-03'
---

## 概要

マイクロサービスアーキテクチャにおいて、クライアントとサービス群の間にAPIゲートウェイを置くことで、ルーティング・リクエスト集約・SSL終端や認証・レート制限などの横断的関心事を一元化できることを解説したガイド。ゲートウェイなしでは複雑なクライアントコードや密結合、レイテンシ増加、攻撃対象領域の拡大などの課題が生じるとし、リバースプロキシやサービスメッシュのIngressゲートウェイ、Azure Application Gateway、Azure Front Door、Azure API Managementなど実装選択肢ごとの得意分野を比較している。
