---
type: case
title: Zillowが毎日1億件の通知をStep Functionsの設定駆動オーケストレーションで配信
title_original: How Zillow runs 100 million daily notifications on AWS Step Functions
ai_relevant: false
company: Zillow
industry: other
cloud:
- aws
patterns: []
components: []
outcome:
  type: productivity
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-zillow-runs-100-million-daily-notifications-on-aws-step-functions/
published_at: '2026-11-11'
---

## 概要

Zillowは1日1億件超のメール・プッシュ通知を、1通知=1つのStep Functions Expressワークフローとして実行する設定駆動の基盤に統合した。キャンペーンごとの重複実装を減らし、立ち上げ速度と一貫性を高めた。
