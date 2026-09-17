---
type: guidance
title: SQLで時系列パターン検出を簡素化するMATCH_RECOGNIZE
title_original: 'Regex for Rows: Simplifying Pattern Detection in SQL with MATCH_RECOGNIZE'
ai_relevant: false
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/regex-rows-simplifying-pattern-detection-sql-matchrecognize
published_at: '2026-09-16'
---

## 概要

Databricks SQL（Lakehouse Real-Time含む）にパブリックプレビューで追加されたMATCH_RECOGNIZE演算子は、正規表現のような記法でイベントデータの時系列パターンを検出できる新しいSQL構文である。不正ログイン検知、株価のV字反転検出、ECのカゴ落ち検知、設備の予兆保全など複数業界の例を通じて、従来LAG/LEADやgaps-and-islandsで複雑なCTEを組む必要があった処理を1つの句に集約できることを示す。
