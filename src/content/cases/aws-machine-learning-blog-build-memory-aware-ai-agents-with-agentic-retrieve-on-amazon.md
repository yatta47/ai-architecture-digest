---
type: announcement
title: Bedrock Managed Knowledge BaseでAgentCoreメモリを使うメモリ対応エージェント
title_original: Build memory-aware AI agents with Agentic Retrieve on Amazon Bedrock Managed Knowledge Base
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- rag
- memory-consolidation
- multi-tenant-rag
- ai-agent
components:
- Amazon Bedrock Managed Knowledge Base
- Amazon Bedrock AgentCore
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-memory-aware-ai-agents-with-agentic-retrieve-on-amazon-bedrock-managed-knowledge-base/
published_at: '2026-11-16'
---

## 概要

Bedrock Managed Knowledge BaseのAgentic Retrieveにmemory設定を加えると、会話保存、事実抽出、検索への反映をサービスが担う。ユーザーACLに基づく文書制御も同じ呼び出しで行える。

## 設計のポイント

- AgentCoreメモリを検索ソースとして並べ、プランナーが必要時に長期記憶を引く。
- userContextでACLに従う文書だけを返し、ユーザー単位の分離を保つ。
- オプトインかつ後方互換で、アプリ側は認証とユーザー情報の受け渡しに専念できる。

## 使いどころ

- フォローアップ質問やユーザー属性を踏まえるサポートアシスタント。
- マルチテナントSaaSの文書チャット。
