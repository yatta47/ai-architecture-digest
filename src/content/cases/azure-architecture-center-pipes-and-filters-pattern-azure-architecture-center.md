---
type: guidance
title: Pipes and Filtersパターンによる処理パイプラインのモジュール分割
title_original: Pipes and Filters pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/pipes-and-filters
published_at: '2026-06-03'
---

## 概要

処理パイプラインを、独立してデプロイ・スケールできる複数のフィルターと、それらをつなぐパイプに分解するPipes and Filtersパターンを解説する。フィルターは自己完結・ステートレスで入出力スキーマにのみ依存するため、順序の入れ替えや再利用、異なるハードウェアでの並列実行がしやすくなる。遅いフィルターだけを並列化・独立スケールすることでスループットを改善できる一方、冪等性や障害時の整合性には注意が必要となる。
