---
type: guidance
title: Bedrock Managed Knowledge Baseの単発RAG・検索専用・エージェント検索の使い分け
title_original: Single-shot and agentic retrieval with Amazon Bedrock Managed Knowledge Base
company: AWS
industry: financial-services
cloud:
- aws
patterns:
- rag
- ai-agent
components:
- Amazon Bedrock Managed Knowledge Base
- AgenticRetrieveStream
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/single-shot-and-agentic-retrieval-with-amazon-bedrock-managed-knowledge-base/
published_at: '2026-11-09'
---

## 概要

Bedrock Managed Knowledge Baseが単発RAGと検索専用に対応し、既存のエージェント検索と同一APIで使えるようになった。銀行の社内規程アシスタントを例に、質問の複雑さに応じて検索の労力を切り替える方法を示す。

## 設計のポイント

- 単純な質問は単発RAG、複数文書の比較はエージェント検索に切り替える。
- 検索専用モードで原文を直接確認できるようにする。
- 反復上限を設定して検索の深さを制御する。

## 使いどころ

- 社内規程やマニュアルのQAアシスタント
