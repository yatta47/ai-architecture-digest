---
type: case
title: Lakebaseのコピーオンライトブランチで全PRに本番相当DBを即時提供するCI/CD
title_original: 'Lakebase Branching for CI/CD: Lessons from 100 PR Databases'
ai_relevant: false
company: Snorkel AI
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/lakebase-branching-cicd-lessons-100-pr-databases
published_at: '2026-10-31'
---

## 概要

Snorkel AIは、PRごとにDatabricks Lakebase（サーバーレスPostgres）のブランチを作成し、約20分かかっていたAurora復元を1分未満の本番相当DB提供に置き換えた。ブランチはコピーオンライトで変更分のみ課金され、TTLで自動削除される。本番データはAWS DMSで継続レプリケーションし、Okta SSOとサービスプリンシパルで認証を分けている。
