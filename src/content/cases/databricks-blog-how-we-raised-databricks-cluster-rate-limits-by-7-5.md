---
type: case
title: Databricksがクラスタ作成APIに適応的並行制限を導入しレート上限を7.5倍に
title_original: How we raised Databricks cluster rate limits by 7.5x
ai_relevant: false
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-we-raised-databricks-cluster-rate-limits-75
published_at: '2026-11-18'
---

## 概要

Databricksのコンピュートプラットフォームは、固定のリクエストレート制限を、システム健全性に応じて調整する適応的並行制限へ置き換えた。有界キューと公平スケジューリングで負荷を吸収し、既定レート上限を7.5倍に引き上げ、顧客別オーバーライドを100件以上削除した。
