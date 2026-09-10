---
type: guidance
title: Lakebase Postgresのコンピュート側キャッシュ改善
title_original: Improving Lakebase Postgres compute cache
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
source_url: https://www.databricks.com/blog/improving-lakebase-postgres-compute-cache
published_at: '2026-09-10'
---

## 概要

ストレージを分離したLakebase Postgresにおいて、共有バッファとOSページキャッシュの二重バッファリングを解消し、オートスケール可能なコンピュート側キャッシュを実装した取り組みを紹介する。本番投入により2倍のスループット、ストレージ層への読み取り削減、レイテンシ低下を達成した。
