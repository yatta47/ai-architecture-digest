---
type: announcement
title: 'LlamaIndexニュースレター: Azure連携・LlamaParse活用事例まとめ'
title_original: LlamaIndex Newsletter 2024-11-26
company: LlamaIndex
industry: cross-industry
cloud:
- azure
patterns:
- rag
- document-processing
- multi-agent-orchestration
components:
- LlamaParse
- Azure OpenAI
- Azure AI Search
- Azure AI Embeddings
- MongoDB
- Redis
- chat-ui
- create-llama
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-11-26
published_at: '2026-07-22'
---

## 概要

LlamaIndexの週次ニュースレターで、Microsoft IgniteでのAzure OpenAI/Azure AI Search連携ソリューション発表、LlamaParseを使った履歴書マッチングやNLP論文解析事例、chat-ui 4.0.0やcreate-llama v0.3.15のリリースなどをまとめている。

## 設計のポイント

- LlamaParseで抽出したPDFをそのままエージェント/RAGパイプラインの入力として再利用する構成を各事例で共通化する
- chat-ui/create-llamaのようなフロントエンド部品をOSS化し、任意のAIプロジェクトに1行で組み込めるようにする

## 使いどころ

- 採用業務での履歴書マッチングなど、ドキュメント解析を伴う業務自動化を検討するチーム
- RAGアプリにセマンティックキャッシュやハイブリッド検索を組み込みたい開発者
