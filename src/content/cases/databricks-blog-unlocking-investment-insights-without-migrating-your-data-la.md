---
type: guidance
title: データを移さずオンプレと外部データを結合するLakehouse Federation
title_original: 'Unlocking Investment Insights Without Migrating Your Data: Lakehouse Federation'
ai_relevant: false
company: Databricks
industry: financial-services
cloud: []
patterns: []
components: []
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/unlocking-investment-insights-without-migrating-your-data-lakehouse-federation
published_at: '2026-10-27'
---

## 概要

オンプレのSQL Serverにある保有銘柄データをLakehouse Federationで参照し、MarketplaceのFactSetデータと1本のSQLで結合してダッシュボードとGenieの自然言語クエリに使う手順である。データは移動せず、中間オブジェクトも作らない。
