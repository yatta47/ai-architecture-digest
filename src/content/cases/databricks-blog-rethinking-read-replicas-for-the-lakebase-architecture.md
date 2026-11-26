---
type: guidance
title: ストレージ共有型で作り直すPostgresリードレプリカ（Lakebase）
title_original: Rethinking read replicas for the Lakebase architecture
ai_relevant: false
company: Databricks
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/rethinking-read-replicas-lakebase-architecture
published_at: '2026-11-26'
---

## 概要

Lakebaseはコンピュートとストレージを分離し、リードレプリカをプライマリと同じストレージに接続する追加コンピュートとして実現する。データを複製せず数秒で起動し、読み取り負荷に応じたオートスケールとゼロスケールができる。
