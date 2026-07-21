---
type: case
title: Samsungが実現したAWS Lambda Response Streamingによるリアルタイム価格配信
title_original: How Samsung achieved real-time pricing with AWS Lambda Response Streaming
ai_relevant: false
company: Samsung
industry: retail
cloud:
- aws
patterns: []
components: []
outcome:
  type: speed
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-samsung-achieved-real-time-pricing-with-aws-lambda-response-streaming/
published_at: '2026-06-15'
---

## 概要

Samsung.comが、1時間ごとのバッチ事前計算で全商品組み合わせの価格をキャッシュしていた従来方式(Data Aggregation)を廃止し、AWS Lambda Response StreamingとAmazon CloudFrontで価格エンジンにリクエスト時に直接問い合わせるステートレスな『Bulk Arbitration Engine』に置き換え、価格のズレとフラッシュセール反映遅延を解消した。
