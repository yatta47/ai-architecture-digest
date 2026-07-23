---
type: guidance
title: マルチテナントRAG推論をセキュアに設計するためのアーキテクチャガイド
title_original: Design a secure multitenant RAG inferencing solution
industry: cross-industry
cloud:
- azure
patterns:
- multi-tenant-rag
- rag
- defense-in-depth
components:
- Azure OpenAI
- Azure AI Search
- Azure Blob Storage
- Azure OpenAI On Your Data
- Foundry Agent Service
- Foundry IQ
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/secure-multitenant-rag
published_at: '2025-10-03'
---

## 概要

RAGを用いたマルチテナントAIアプリケーションにおいて、各テナントやユーザーが認可されたグラウンディングデータのみを参照できるようにするための設計指針を解説する記事。オーケストレーター型とAzure OpenAIのOn Your Data機能による直接データアクセス型の2つの単一テナントRAGアーキテクチャを比較し、テナント専用ストア・マルチテナントストア・共有ストアが混在する状況でのデータアクセス制御の考え方を示す。

## 設計のポイント

- オーケストレーターを介してデータストアからグラウンディングデータを取得する構成にすると、取得ロジックや認可制御を柔軟にカスタマイズできる
- Azure OpenAIのOn Your Data機能のようにモデル提供サービスが直接データストアにアクセスする構成では、マルチテナントの認可ロジックをそのサービス側でサポートしている必要がある
- テナントデータをテナント専用ストア・複数テナント共有ストア・全テナント共有ストアのいずれに置くかを明確にし、ユーザーには自身が認可されたデータのみが見えるようにフィルタリングする
- ユーザーのリクエストには認証トークンを付与してオーケストレーターAPIに渡し、認可済みユーザーのみがクエリを実行できるようにする

## 使いどころ

- 複数の顧客企業・組織がテナントとして同居するSaaS型RAGアプリケーションを設計するアーキテクト
- テナントごとのデータ分離とアクセス制御を厳密に行う必要がある業務システムの構築担当者
- Azure OpenAIのOn Your Data機能からFoundry Agent Service/Foundry IQへの移行を検討しているチーム
