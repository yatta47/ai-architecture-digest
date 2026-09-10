---
type: guidance
title: DynamoDBリースによるリアルタイムストリーミングワーカーの耐障害設計
title_original: Building resilient real-time streaming workers with Amazon DynamoDB leases
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
source_url: https://aws.amazon.com/blogs/architecture/building-resilient-real-time-streaming-workers-with-amazon-dynamodb-leases/
published_at: '2026-09-10'
---

## 概要

数百件の永続WebSocket接続を保持するワーカーフリートで、障害発生時に接続の所有権を自動的に引き継ぐリース方式をAmazon DynamoDBの条件付き書き込みで実装する方法を解説する。ECS/Fargate上でのオーファン接続の再割り当てとローリングデプロイ時のダウンタイム最小化を扱う。
