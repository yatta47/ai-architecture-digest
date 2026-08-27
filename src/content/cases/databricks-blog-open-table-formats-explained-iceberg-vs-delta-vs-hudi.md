---
type: guidance
title: オープンテーブルフォーマット解説：Iceberg・Delta Lake・Hudiの違い
title_original: 'Open Table Formats Explained: Iceberg vs. Delta vs. Hudi'
ai_relevant: false
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/open-table-formats
published_at: '2026-08-25'
---

## 概要

Apache Iceberg・Delta Lake・Apache Hudiはオブジェクトストレージ上のデータにACIDトランザクション・スキーマ進化・タイムトラベルを付与するメタデータレイヤーであり、データレイクをデータベースのように扱えるレイクハウスの基盤となる。それぞれの出自（Netflix/Databricks/Uber）に応じた強みの違いを整理しつつ、Delta Lake UniFormやUnity Catalogなどの相互運用機能により3フォーマット間の垣根が薄まりつつあることを解説する。
