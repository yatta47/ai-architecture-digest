---
type: opinion
title: LLMの知識の古さにどう対処するか：RAGとファインチューニングの考え方
title_original: 'ChatGPT’s Knowledge Is Two Year’s Old: What to do if you’re building applications'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- context-engineering
components:
- ChatGPT
- LlamaIndex
- LangChain
- Semantic Kernel
- DSPy
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/chatgpts-knowledge-is-two-year-s-old-what-to-do-if-you-re-building-applications-72ceacde135c
published_at: '2023-09-01'
---

## 概要

ChatGPTの知識カットオフを題材に、最新情報が必要なアプリはRAG（検索して渡す）で補うのが定石だと解説する。最新性が不要な用途もあると指摘する。

## 設計のポイント

- 文脈長と従量課金の制約から、全情報を渡さず関連部分だけ検索して渡す。
- ファインチューニングは手間とデータが多く要るため、RAGとの使い分けを見極める。
- 用途に最新性が本当に必要かを先に判断する。

## 使いどころ

- LLMアプリの設計を始める非専門の開発者向け。
- RAG導入の理由を社内に説明したい場面。
