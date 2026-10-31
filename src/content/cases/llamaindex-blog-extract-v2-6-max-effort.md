---
type: announcement
title: LlamaIndex Extractのagentic_plusに高品質重視のmax effortを追加
title_original: 'Extract v2.6: max effort'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- cost-optimization
components:
- LlamaIndex Extract
- LlamaIndex agentic_plus
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-max-effort-for-extract-agentic-plus
published_at: '2026-10-31'
---

## 概要

LlamaIndexはExtractのagentic_plus層に、複雑な文書の抽出品質を最大化するmax effortを追加した。ExtractBench ProのValue F1は77.7から94.3に上がるが、計算量に応じた従量課金でコストは通常より増える。

## 設計のポイント

- 抽出の欠落や誤りのコストが高い場面に限り、計算量と課金を増やして品質を取りにいく。
- 文書と抽出スキーマで概念実証を行い、予算内の最適な層を選ぶ。

## 使いどころ

- 契約書や帳票など誤抽出の損失が大きい文書処理。
- 品質とコストの曲線を見て抽出設定を決めたい導入担当者。
