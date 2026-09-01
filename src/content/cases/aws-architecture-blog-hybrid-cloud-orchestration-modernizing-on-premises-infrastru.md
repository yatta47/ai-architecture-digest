---
type: guidance
title: サーバーレスで数千台のオンプレサーバーとEKS Anywhereクラスタを一元オーケストレーション
title_original: 'Hybrid cloud orchestration: Modernizing on-premises infrastructure management with AWS'
ai_relevant: false
industry: cross-industry
cloud:
- aws
- on-prem
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/hybrid-cloud-orchestration-modernizing-on-premises-infrastructure-management-with-aws/
published_at: '2026-09-01'
---

## 概要

地理的に分散した数千台規模のオンプレミスサーバーとEKS Anywhereクラスタを、AWS Lambda・Step Functions・DynamoDBによるイベント駆動オーケストレーションエンジンで一元管理するアーキテクチャを解説する。RedfishのベンダーニュートラルAPIでハードウェア操作を標準化し、拠点ごとにばらつきがちなライフサイクル管理を統一する。
