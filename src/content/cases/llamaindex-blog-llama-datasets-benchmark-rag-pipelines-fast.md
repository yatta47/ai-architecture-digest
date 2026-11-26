---
type: announcement
title: 用途に近い評価データでRAGを測るLlama Datasets
title_original: Introducing Llama Datasets
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- eval
- rag
components:
- Llama Datasets
- LlamaHub
- RagEvaluatorPack
- LlamaIndex
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-llama-datasets-aadb9994ad9e
published_at: '2023-12-04'
---

## 概要

質問・回答と根拠コンテキストを組にしたコミュニティ投稿型の評価データセット群を公開した。学術ベンチマークは個別用途に汎化しにくいため、自分の領域に近いデータを選んでRAGを測定できる。

## 設計のポイント

- 高度な手法で最適化する前に評価基盤を先に整える。
- 本番の用途を反映した評価データを選ぶか自作する。
- 予測生成と指標計算を分け、パイプラインを差し替えて同条件で比較する。

## 使いどころ

- RAGの変更効果を定量的に判断したいチーム。
