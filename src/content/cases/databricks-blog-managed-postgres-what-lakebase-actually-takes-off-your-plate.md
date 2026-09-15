---
type: guidance
title: マネージドPostgresが本当に肩代わりすべき運用範囲とLakebaseの実装範囲
title_original: 'Managed Postgres: what Lakebase actually takes off your plate'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/managed-postgres
published_at: '2026-09-14'
---

## 概要

Databricks LakebaseがPostgreSQLをサーバーレス基盤上で提供し、自動スケーリング・scale-to-zero・自動スナップショット・ポイントインタイムリカバリ・ブランチング・pgvector/PostGISといった拡張をリージョン内でマネージドに提供する範囲を解説。クロスリージョンの災害復旧は依然として顧客側の管理が必要。
