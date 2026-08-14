---
type: case
title: Bosch L.OSによるインド物流市場向けサーバーレス車両トラッキング基盤
title_original: 'Serverless vehicle tracking at scale: Bosch L.OS on AWS'
ai_relevant: false
company: Bosch Mobility Platform Solutions
industry: logistics
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/serverless-vehicle-tracking-at-scale-bosch-l-os-on-aws/
published_at: '2026-08-14'
---

## 概要

Bosch Mobility Platform Solutionsは、インドの分散したスポット物流市場で乱立する各社テレマティクス提供者のデータ形式やプロトコルの違いを統一するため、サーバーレスの車両トラッキング基盤L.OSをAWS上に構築した。ECS FargateのTracking Connectorがプロトコル標準化とルーティングを担い、Lambdaアダプタが各プロバイダAPIとの変換を行い、MSKが位置情報更新の非同期配信を担う構成。
