---
type: case
title: 本番から直接分岐させるLakebaseブランチCI/CDパターン
title_original: 'Branching databases like code: a CI/CD pattern for Lakebase in production'
ai_relevant: false
company: Glaspoort
industry: telecom
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/branching-databases-code-cicd-pattern-lakebase-production-glaspoort
published_at: '2026-07-20'
---

## 概要

オランダの光ファイバー事業者Glaspoortは、DatabricksのOLTPデータベースLakebaseを使い、開発・受け入れ環境を積み重ねではなく本番から直接分岐させることで、環境をリフレッシュするたびに配下のブランチをすべて作り直す「reset-from-parentの罠」を回避した。PRごとに本番のコピーオンライトブランチを使い捨てで作成し、マイグレーションをライブアプリイメージに対して検証してから昇格させるCI/CDフローを構築している。
