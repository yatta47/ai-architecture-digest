---
type: guidance
title: IcebergカタログのREGISTER/UNREGISTERでカタログロックインを避ける
title_original: 'Unlocking data portability: preventing catalog lock-in with REGISTER and UNREGISTER APIs'
ai_relevant: false
company: Databricks
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/unlocking-data-portability-preventing-catalog-lock-register-and-unregister-apis
published_at: '2026-10-05'
---

## 概要

Iceberg RESTカタログ仕様のREGISTERと新設UNREGISTERにより、データを複製せずにテーブルの管理をカタログ間で移せる。旧カタログが先に管理権を手放すため、スプリットブレインを防げる。
