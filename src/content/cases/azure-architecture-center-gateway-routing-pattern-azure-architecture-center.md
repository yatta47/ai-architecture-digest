---
type: guidance
title: 単一エンドポイントで複数サービス・バージョンを束ねるGateway Routing
title_original: Gateway Routing pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/gateway-routing
published_at: '2026-02-24'
---

## 概要

クライアントが複数サービス・複数インスタンス・複数バージョンを意識せず単一エンドポイントで済むようにするGateway Routingパターンを解説する。Blue-Greenデプロイやリージョン間のレイテンシ最適化など、ゲートウェイでのL7ルーティング活用例を示す。
