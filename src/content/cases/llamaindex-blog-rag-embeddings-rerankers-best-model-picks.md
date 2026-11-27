---
type: guidance
title: RAGの埋め込みモデルとリランカーの組み合わせを評価で選ぶ
title_original: 'Boosting RAG: Picking the Best Embedding & Reranker models'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- eval
components:
- LlamaIndex
- OpenAI Embeddings
- CohereRerank
- bge-reranker-large
- JinaAI-v2-base-en
- Anthropic
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83
published_at: '2023-11-03'
---

## 概要

LlamaIndexの検索評価モジュールで、埋め込みモデルとリランカーの組み合わせをヒット率とMRRで比較する手順を解説する。広めに取得してからリランカーで絞る構成を使う。

## 設計のポイント

- top-10を取得してリランカーでtop-5に絞る二段検索にする。
- 評価対象と異なる提供元のLLMで質問を合成し、評価の偏りを抑える。
- 最適な組み合わせはデータ依存なので、自社データで測って選ぶ。

## 使いどころ

- RAGの検索構成を根拠をもって選定したい開発者。
