---
type: guidance
title: マイクロサービスにおけるAPI設計指針：RESTとRPCの選び方
title_original: API design
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/microservices/design/api-design
published_at: '2025-11-20'
---

## 概要

マイクロサービス間のデータ交換はメッセージまたはAPI呼び出しを介して行われるため、良好なAPI設計がアーキテクチャの要となる。記事はクライアント向けの公開APIとサービス間通信用のバックエンドAPIを区別し、REST over HTTPとgRPC/Avro/Thriftなどのバイナリプロトコルのトレードオフ、IDLやシリアライゼーション形式の選択基準を解説している。副作用を伴う操作の冪等性確保や非同期処理でのHTTP 202応答の活用など、実装上の設計指針も示している。
