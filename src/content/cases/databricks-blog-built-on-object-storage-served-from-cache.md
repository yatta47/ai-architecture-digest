---
type: case
title: オブジェクトストレージ上のPostgresを99%超キャッシュで配信する設計
title_original: Built on object storage, served from cache
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
source_url: https://www.databricks.com/blog/built-object-storage-served-cache
published_at: '2026-11-17'
---

## 概要

Lakebase Postgresでは、ページ読み取りの99.46%がコンピュートのローカルキャッシュで処理され、オブジェクトストレージへの到達は極めて稀である。階層化した読み取り経路でレイテンシ懸念を解消している。AI/LLMは主題でないため軽量カードとする。
