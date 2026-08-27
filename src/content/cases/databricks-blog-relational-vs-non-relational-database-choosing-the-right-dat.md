---
type: guidance
title: リレーショナルDBと非リレーショナルDBの選び方
title_original: 'Relational vs. Non-Relational Database: Choosing the Right Data Model'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/relational-vs-non-relational-database
published_at: '2026-08-24'
---

## 概要

リレーショナルデータベースはスキーマ強制とACID特性で整合性を担保し垂直スケールする一方、非リレーショナルデータベースは柔軟なデータモデルと水平スケールでスループットと可用性を優先する。銀行・医療・ECのような複雑なクエリと厳密な検証が必要な基幹系にはリレーショナルDBを、SNSやIoTのような大量分散ワークロードには非リレーショナルDBを使い分けるべきだと整理する。
