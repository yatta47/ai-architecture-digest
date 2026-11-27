---
type: guidance
title: 合成データで埋め込みモデルを調整しRAG検索を改善する手順
title_original: Fine-tuning Embeddings for RAG with Synthetic Data
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- fine-tuning
- rag
- eval
components:
- LlamaIndex
- sentence-transformers
- bge-small-en
- Hugging Face
- text-embedding-ada-002
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/fine-tuning-embeddings-for-rag-with-synthetic-data-e534409a3971
published_at: '2023-08-25'
---

## 概要

ラベルなしの文書からLLMで質問を生成し、埋め込みモデルをファインチューニングする一連の手順を解説する。検索評価指標が5〜10%向上したとする。

## 設計のポイント

- 各チャンクが答えになる仮想質問をLLMに作らせ、正例ペアを人手なしで用意する。
- 小型のオープン埋め込みモデルを基点にし、GPUなしで学習できる規模に抑える。
- 学習用と評価用のデータを分け、調整前後を検索指標で比較する。

## 使いどころ

- 専門領域の文書で検索の当たりが悪いRAGを改善したいチーム向け。
- 自前ホストの埋め込みモデルで商用APIに近い性能を狙う場面。
