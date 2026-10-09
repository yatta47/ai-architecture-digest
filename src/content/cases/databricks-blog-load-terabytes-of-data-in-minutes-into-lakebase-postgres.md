---
type: announcement
title: LTAPでLakebase Postgresへ1TBを5分未満でロード
title_original: Load terabytes of data in minutes into Lakebase Postgres
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
source_url: https://www.databricks.com/blog/load-terabytes-data-minutes-lakebase-postgres
published_at: '2026-10-08'
---

## 概要

LTAPアーキテクチャにより、Sparkが並列にPostgresページとインデックスを作ってストレージへ直接書き、プライマリはマニフェストだけをWALで公開する。1TBのロードが5分未満で、従来比最大147倍高速になる。データベースのバルクロードの話でAIは中心ではない。
