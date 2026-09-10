---
type: guidance
title: AWS FISによるSQSを使ったアプリケーションのレジリエンステスト
title_original: Testing application resilience with Amazon SQS and AWS Fault Injection Service
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
source_url: https://aws.amazon.com/blogs/architecture/testing-application-resilience-with-amazon-sqs-and-aws-fault-injection-service/
published_at: '2026-09-09'
---

## 概要

AWS Fault Injection Service（FIS）を使い、SQSへのアクセスを段階的に拒否するカオス実験を組み立てて、アプリケーションの障害処理（フェイルファスト・サーキットブレーカー・バッファリング）とオブザーバビリティが実際に機能するかを検証する方法を解説する。
