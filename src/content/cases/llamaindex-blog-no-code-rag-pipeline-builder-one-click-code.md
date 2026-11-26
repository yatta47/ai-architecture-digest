---
type: case
title: RAG構成をGUIで試してコードを生成するノーコードツールRAGArch
title_original: 'RAGArch: No-Code RAG Pipeline Builder'
industry: cross-industry
cloud: []
patterns:
- rag
- eval
components:
- RAGArch
- LlamaIndex
- Streamlit
- Hugging Face Spaces
- Pinecone
- Qdrant
- Gemini Pro
- Cohere
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/ragarch-building-a-no-code-rag-pipeline-configuration-one-click-rag-code-generation-tool-powered-b6e8eeb70089
published_at: '2024-02-02'
---

## 概要

RAGArchは、LLM・埋め込み・ノード分割・応答合成・ベクトルストアを画面で選び、自分のデータで試して、その構成のPythonコードを出力するツール。

## 設計のポイント

- RAGの各構成要素を差し替え可能にし、同じデータで比較できるようにする。
- 検証した設定からコードを生成して実装へ引き継ぐ。

## 使いどころ

- RAGの構成選定を素早く比較したい開発者。
- RAGを学び始めた人。
