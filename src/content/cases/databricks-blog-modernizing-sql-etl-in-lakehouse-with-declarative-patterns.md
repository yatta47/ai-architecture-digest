---
type: announcement
title: Databricks LakehouseへSQLエディタから使える宣言型ETL（APPEND/AUTO CDC/REPLACE WHERE）を追加
title_original: Modernizing SQL ETL in Lakehouse with Declarative Patterns
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/modernizing-sql-etl-lakehouse-declarative-patterns
published_at: '2026-08-25'
---

## 概要

Databricksは、追記専用の取り込み・CDC・部分的な上書きといった定型的なETLパターンを、専用のパイプライン環境ではなく通常のSQLエディタから宣言的に記述できる機能をLakehouseに追加した。自動増分計算エンジンEnzymeを使ったREPLACE WHEREはベンチマークで従来比3.4倍高速・2.5倍低コストになったとしており、bsport社は宣言的AUTO CDCによってデータ取り込みの疎結合化と信頼性向上を実現したとコメントしている。
