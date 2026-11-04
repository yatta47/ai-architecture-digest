---
type: announcement
title: DatabricksのUNIQUE制約とRELYによるクエリ最適化
title_original: Declare and optimize with unique constraints on Databricks
ai_relevant: false
company: Databricks
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/declare-and-optimize-unique-constraints-databricks
published_at: '2026-11-03'
---

## 概要

DatabricksのUNIQUE制約がPublic Previewになり、複数の一意性保証を宣言できる。検証後にRELYを付けるとオプティマイザが冗長な結合やDISTINCT集計を除去し、10TBのTPC-DSで最大12倍高速化したとする。
