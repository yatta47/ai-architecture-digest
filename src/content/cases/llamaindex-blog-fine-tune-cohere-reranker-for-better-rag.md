---
type: guidance
title: 自社ドメイン向けにCohereリランカーをファインチューニングする手順
title_original: Improving Retrieval Performance by Fine-tuning Cohere Reranker with LlamaIndex
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- fine-tuning
- eval
components:
- Cohere Rerank
- LlamaIndex
- GPT-4
- Cohere embed-english-v3.0
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/improving-retrieval-performance-by-fine-tuning-cohere-reranker-with-llamaindex-16c0c1f9b33b
published_at: '2023-11-16'
---

## 概要

LlamaIndexを使い、チャンクからLLMで質問を生成してCohereのカスタムリランカーを学習し、検索性能を評価する手順を解説する。ハードネガティブなし、ランダム選定、コサイン類似度選定の3種のデータセットを作る。

## 設計のポイント

- 学習用の質問とパッセージの組はLLMで合成し、人手のラベル付けを省く。
- ハードネガティブの作り方を複数用意し、評価で比較して決める。
- 学習に使わない別文書で評価し、汎化を確認する。

## 使いどころ

- 汎用リランカーでは専門文書の検索精度が足りないRAG開発者。
