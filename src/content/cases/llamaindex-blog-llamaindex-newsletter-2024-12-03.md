---
type: announcement
title: 'LlamaIndex: LlamaParseのAzure OpenAI対応'
title_original: LlamaIndex Newsletter 2024-12-03
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
- eval
components:
- Azure OpenAI
- Azure AI Search
- LlamaParse
- Ragas
- MongoDB
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-12-03
published_at: '2024-12-03'
---

## 概要

Azure OpenAIエンドポイントをLlamaParseで利用可能にし、Azure AI Searchと組み合わせたRAGを安全に構成できるようにした告知。RAG評価やCXLメモリによる高速化のガイドも紹介。

## 設計のポイント

- Azure OpenAIの自社エンドポイントを使い、コンプライアンスを保ってパースする
- Ragasなどで文脈精度・再現率・回答関連性を評価してから本番へ出す
- CXLメモリでRAGのQPSを向上させる

## 使いどころ

- Azure環境で文書RAGを構築する場面
- RAGの品質評価指標を整備する場面
