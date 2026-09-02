---
type: case
title: Databricks管理Postgresの脆弱性、外部研究者との協調的開示で迅速に修正
title_original: Collaboration makes us all stronger
ai_relevant: false
company: Databricks
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/collaboration-makes-us-all-stronger
published_at: '2026-09-01'
---

## 概要

Databricksはバグバウンティ経由で、管理型PostgresのLakebase PostgresやNeonが利用するPostGIS拡張address_standardizerのメモリ安全性の脆弱性を外部研究者から報告された。マイクロVMアーキテクチャによりテナント間の影響は防げていたが、上流OSSの問題であっても自社の責任として即座にダウンストリームパッチを配布し、後にアップストリームへも修正を還元した。
