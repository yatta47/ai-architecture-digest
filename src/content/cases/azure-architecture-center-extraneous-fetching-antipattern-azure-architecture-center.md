---
type: guidance
title: 不要なデータ取得(Extraneous Fetching)アンチパターンとその回避策
title_original: Extraneous Fetching antipattern
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/antipatterns/extraneous-fetching/
published_at: '2025-12-09'
---

## 概要

業務処理に必要な量を超えてデータを取得してしまう「Extraneous Fetching」アンチパターンを解説する記事。Entity Frameworkを例に、全カラム取得後にアプリ側でフィルタや集計を行うことで不要なI/Oとメモリ負荷が発生する典型例を示す。対策として、必要な列だけを射影するクエリ、データベース側での集計、IQueryableを維持したクエリ設計、ページネーションを推奨している。
