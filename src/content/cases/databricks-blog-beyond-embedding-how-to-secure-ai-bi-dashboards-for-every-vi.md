---
type: guidance
title: 1つの埋め込みダッシュボードを閲覧者ごとに行レベルで権限分離する設計パターン
title_original: 'Beyond embedding: How to secure AI/BI dashboards for every viewer'
ai_relevant: false
company: Databricks
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/beyond-embedding-how-secure-aibi-dashboards-every-viewer
published_at: '2026-09-09'
---

## 概要

顧客向けアプリに埋め込んだダッシュボードで、パートナーごと・社内チームごとに見える行を制限する設計パターンを解説する。単一のエンタイトルメントテーブルと署名付き埋め込みトークンの__aibi_external_valueで、顧客ごとにダッシュボードを複製せず1つのビューで権限分離を実現する。
