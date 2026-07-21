---
type: case
title: Salesforce Data 360、任意スキーマで月間1000兆件を処理するセグメンテーション基盤
title_original: How Data 360 Segmentation Processes a Quadrillion Records Across Arbitrary Customer Data Models
ai_relevant: false
company: Salesforce
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: reliability
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-data-360-segmentation-processes-a-quadrillion-records-across-arbitrary-customer-data-models/
published_at: '2026-06-15'
---

## 概要

Salesforce Data 360のセグメンテーションエンジンが、顧客ごとに全く異なるスキーマ・関係グラフを持つ環境で月間1000兆件のレコードを処理する仕組みを解説。ワークロードサイズの事前見積り、SLA考慮のリトライ、レート制限、動的リソース配分により、過剰プロビジョニングなしに約99.95%の信頼性を維持する。
