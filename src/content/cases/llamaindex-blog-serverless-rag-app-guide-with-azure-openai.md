---
type: guidance
title: LlamaIndexとAzure OpenAIで作るサーバーレスRAGアプリ
title_original: Serverless RAG App Guide With Azure OpenAI
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- rag
components:
- LlamaIndex
- Azure OpenAI
- Azure Container Apps
- Azure Managed Identity
- Azure Developer CLI
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-a-serverless-rag-application-with-llamaindex-and-azure-openai
published_at: '2024-08-27'
---

## 概要

LlamaIndexとAzure OpenAIを使い、Azure Developer CLIでAzure Container AppsへデプロイするRAGサンプルの手引き。取り込みと問い合わせ処理の2つの流れと、TypeScript版・Python版のテンプレートを示す。

## 設計のポイント

- 取り込み(分割・埋め込み・索引作成)と問い合わせ処理を別の流れとして分ける。
- Managed Identityを使い、APIキーなどの資格情報を開発者が扱わない構成にする。
- azdテンプレートでアプリとインフラをまとめてデプロイする。

## 使いどころ

- Azure上で社内文書RAGを素早く試作したい開発者。
- 資格情報レスの構成を雛形から始めたい場合。
