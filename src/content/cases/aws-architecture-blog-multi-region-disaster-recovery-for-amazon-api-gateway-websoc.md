---
type: guidance
title: API Gateway WebSocket APIのマルチリージョン災害対策パターン
title_original: Multi-region disaster recovery for Amazon API Gateway WebSocket APIs
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/multi-region-disaster-recovery-for-amazon-api-gateway-websocket-apis/
published_at: '2026-10-14'
---

## 概要

WebSocket接続がリージョンに固定される問題に対し、Route 53フェイルオーバーとDynamoDBグローバルテーブルで状態を複製し、クライアント再接続で復旧するアクティブ/パッシブ構成を示す。カナリアによる障害検知も併用する。
