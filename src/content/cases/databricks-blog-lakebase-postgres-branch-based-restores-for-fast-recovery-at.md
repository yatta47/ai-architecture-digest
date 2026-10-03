---
type: announcement
title: コンピュートとストレージ分離で実現するPostgresのブランチ型高速リストア
title_original: 'Lakebase Postgres: Branch-Based Restores for Fast Recovery at Scale'
ai_relevant: false
company: Databricks
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/lakebase-postgres-branch-based-restores-fast-recovery-scale
published_at: '2026-10-01'
---

## 概要

Databricks の Lakebase Postgres は、コンピュートとストレージを分離し履歴をオブジェクトストレージ上の不変タイムラインとして保持することで、リストアを「指定時刻でブランチを作るメタデータ操作」に置き換える。従来のPITRが要する新規インスタンス作成・スナップショット取得・WAL再生を不要にし、100TBでも数秒で復旧できるとする。AIエージェントによるブランチ/undo操作にも使えると述べている。
