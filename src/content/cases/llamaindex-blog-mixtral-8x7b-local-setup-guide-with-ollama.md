---
type: guidance
title: OllamaとQdrantでMixtralを完全ローカルで動かすRAG
title_original: Running Mixtral 8x7b locally with LlamaIndex and Ollama
industry: cross-industry
cloud:
- on-prem
patterns:
- rag
components:
- Mixtral 8x7B
- Ollama
- LlamaIndex
- Qdrant
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/running-mixtral-8x7-locally-with-llamaindex-e6cebeabe0ab
published_at: '2023-12-21'
---

## 概要

Ollamaで取得したMixtral 8x7Bに、LlamaIndexとQdrantを組み合わせて自分のデータを参照させる手順。埋め込みもローカルで計算するため外部APIに依存しない（Mixtralの実行には約48GBのRAMが必要）。

## 設計のポイント

- LLM・埋め込み・ベクトルDBをすべてローカルに置き、データを外に出さない。
- メモリが足りない環境ではMistral 7Bに差し替える。

## 使いどころ

- 機密データを外部に送れない開発者の試作。
- オフラインでRAGを検証したい場面。
