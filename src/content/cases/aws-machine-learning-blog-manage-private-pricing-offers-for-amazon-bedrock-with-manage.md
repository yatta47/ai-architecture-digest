---
type: guidance
title: Bedrockサードパーティモデルの個別価格オファーをマネージドエンタイトルメントで一括有効化
title_original: Manage private pricing offers for Amazon Bedrock with managed entitlements
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/manage-private-pricing-offers-for-amazon-bedrock-with-managed-entitlements/
published_at: '2026-10-13'
---

## 概要

AWS Marketplaceの個別価格オファー(MPPO)で購入したBedrock上のサードパーティモデルを、複数アカウントへ配布するためのLicense Managerグラント有効化手順を解説する。ワンタイム用のスクリプトと、EventBridge+LambdaによるCDK自動化の2経路を示す。
