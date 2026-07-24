---
type: guidance
title: OpenAI Responses APIによるRAGベースのマルチツールオーケストレーション
title_original: Multi-Tool Orchestration with RAG approach using OpenAI's Responses API
industry: cross-industry
cloud:
- aws
patterns:
- rag
- multi-tool-orchestration
components:
- OpenAI Responses API
- Pinecone
- text-embedding-3-small
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/responses_api/responses_api_tool_orchestration/
published_at: '2025-03-28'
---

## 概要

OpenAIのResponses APIを使い、ユーザーの質問内容に応じて内蔵のファイル検索・Web検索や外部ベクトルデータベース（Pinecone）を動的に使い分けるRAGベースのツールオーケストレーションの構築方法を示すクックブックである。医療推論データセットを例に、埋め込み生成からPineconeへの格納、関数呼び出しによる検索までの流れを解説する。

## 設計のポイント

- クエリの内容に応じて内蔵ツール（file_search/Web検索）と外部ベクトルDBへの関数呼び出しを動的にルーティングする
- Pineconeなど外部ベクトルストアと内蔵file_searchを組み合わせて柔軟な検索・生成基盤を構築する

## 使いどころ

- 社内文書と一般知識の両方に答える必要があるQAシステムの構築
- 医療など特定ドメインの専門知識をベクトル検索で補強したい生成AIアプリケーション
