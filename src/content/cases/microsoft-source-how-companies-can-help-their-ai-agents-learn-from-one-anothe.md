---
type: guidance
title: エージェント同士が学び合うための共有知識基盤「ナレッジスパイン」
title_original: How companies can help their AI agents learn from one another
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- multi-agent-orchestration
- context-engineering
- memory-consolidation
components: []
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/copilot/blog/2026/10/27/the-ai-advantage-your-company-can-keep/
published_at: '2026-10-27'
---

## 概要

Keystoneとの調査(200社超)から、エージェントが使う文脈と、作業から得た修正・テスト・教訓を保存し更新する共有システム「ナレッジスパイン」を提唱する。実践が多い企業ほど利益率とROAの伸びが大きいが、基盤を整えた企業は3%にとどまり、相関であって因果ではない。

## 設計のポイント

- エージェントが参照する文脈と、作業で得た修正・教訓を同じ共有基盤に蓄積する。
- エージェントの学習内容を自社固有の資産として扱う。

## 使いどころ

- 複数エージェントを運用し、現場で得た知見を組織全体に還流したい企業。
- エージェント活用の成熟度を自己評価したい経営・DX部門。
