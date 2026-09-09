---
type: guidance
title: Amazon Quickにおけるユーザー単位カスタム権限の自動付与パターン
title_original: Automate user-level custom permissions for Amazon Quick
ai_relevant: false
company: AWS
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/automate-user-level-custom-permissions-for-amazon-quick/
published_at: '2026-09-09'
---

## 概要

Amazon Quick（QuickSight）環境が拡大する中で最小権限原則を維持するため、ユーザーライフサイクルの各段階でカスタム権限を自動付与する4つのアーキテクチャパターンを解説する。API単発呼び出しからEventBridge/Lambdaによるイベント駆動、既存ユーザーへの遡及一括更新まで、シナリオごとの使い分けを示す。
