---
type: opinion
title: 'LTAPに関する誤解の整理: Lakebaseは単一コピーでPostgresと分析を両立'
title_original: Dispelling LTAP myths
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
source_url: https://www.databricks.com/blog/dispelling-ltap-myths
published_at: '2026-11-12'
---

## 概要

LakebaseのLTAPは、レイクをデータベースのストレージとして使い、運用データの単一コピーでPostgresと分析の両方を提供する設計である。LTAPをCDCやレプリケーションとみなす等の4つの誤解に対し、点参照はPostgresのヒープページ、スキャンはParquetから読む仕組みを説明する。
