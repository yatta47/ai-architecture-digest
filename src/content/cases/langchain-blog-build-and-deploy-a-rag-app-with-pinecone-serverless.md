---
type: guidance
title: Pinecone ServerlessとLangServeで作るRAGアプリの本番デプロイ
title_original: Build and deploy a RAG app with Pinecone Serverless
industry: cross-industry
cloud: []
patterns:
- rag
components:
- Pinecone Serverless
- LangServe
- LangSmith
- Cohere
- GPT-4
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/pinecone-serverless
published_at: '2026-06-15'
---

## 概要

Pinecone Serverlessの登場により、固定インデックス管理と月額課金の課題を解消したRAGアプリの構築・デプロイ方法を解説するチュートリアル。LCELで組んだRAGチェーンをLangServeでWebサービス化し、LangSmithで入出力を観測することで、プロトタイプから本番運用までのギャップを埋める。

## 設計のポイント

- ベクトルストアをサーバーレス化し、固定インデックス管理・固定月額課金からusage-basedへ移行する
- LCELで構成したRAGチェーンをそのままLangServeでWebサービス化し、prototypeとproductionのギャップを埋める
- LangSmithでRAGチェーンの入出力を継続的に観測し、本番運用の可視性を確保する

## 使いどころ

- プロトタイプのRAGを最小構成で本番デプロイまで持っていきたいチーム
- ベクトルストアの固定費・インデックス管理コストを避けたい場合
