---
type: announcement
title: LlamaIndexとAzure AIで構築するエンドツーエンドRAG/エージェントスタック
title_original: Announcing the LlamaIndex integration with Azure AI
industry: cross-industry
cloud:
- azure
patterns:
- rag
- ai-agent
- document-processing
components:
- Azure OpenAI Service
- Azure AI Search
- Azure AI Embeddings
- Azure Doc Store
- Azure KV Store
- Azure Chat Store
- Azure Code Interpreter
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/announcing-the-llamaindex-integration-with-azure-ai
published_at: '2026-07-23'
---

## 概要

LlamaIndexとMicrosoftの協業により、Azure OpenAI ServiceとAzure AI Search、Azure Doc/KV/Chat Storeを組み合わせたRAGおよびエージェント向けのエンドツーエンドスタックがAzure上で利用可能になったことを発表。AI App Template Galleryへのテンプレート提供により迅速な本番導入も可能にする。

## 設計のポイント

- LLM本体はAzure OpenAI Serviceに、ベクトル検索はAzure AI Searchに委ね、LlamaIndexで両者を統合するRAG構成をとる
- Azure Doc Store/KV Storeで新規データの差分ロードを行い、Azure Chat Storeでチャットの永続メモリを実現する
- Azure Code Interpreterや音声合成・画像認識・翻訳のエージェントツールをLlamaIndexのWorkflowsから呼び出せる構成にする

## 使いどころ

- Azure上でRAGアプリケーションを迅速に構築したいチーム
- チャット応答に永続メモリやコード実行・画像認識などのツールを組み合わせたエージェントを作りたい開発者
