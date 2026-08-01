---
type: case
title: Lakebase上のBackstageとUnity Catalogを連携させたゼロETLのFinOps基盤
title_original: Backstage with Lakebase, Part 3
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
source_url: https://www.databricks.com/blog/backstage-lakebase-part-3
published_at: '2026-07-31'
---

## 概要

DatabricksはBackstage開発者ポータルをLakebase（ブランチ可能なPostgres）上で稼働させ、Lakehouse FederationでUnity Catalogの請求データと結合することで、インフラ所有者情報とクラウドコストをETL無しの単一SQLクエリで突き合わせられるようにした。ワークロードごとに計算資源を分離しているため、FinOps分析クエリが本番ポータルの応答性能（55〜65ms）に影響を与えない。
