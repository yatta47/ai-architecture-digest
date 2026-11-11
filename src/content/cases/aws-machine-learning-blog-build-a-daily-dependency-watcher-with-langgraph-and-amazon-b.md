---
type: guidance
title: LangGraphとAgentCore Web Searchで作る日次の依存関係ウォッチャー
title_original: Build a daily dependency watcher with LangGraph and Amazon Bedrock AgentCore web search
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- parallel-execution
- guardrails
- context-engineering
components:
- Amazon Bedrock AgentCore
- LangGraph
- LangChain
- AWS Lambda
- Amazon ECS
- AgentCore Gateway
- MCP
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-daily-dependency-watcher-with-langgraph-and-amazon-bedrock-agentcore-web-search/
published_at: '2026-11-10'
---

## 概要

AgentCoreのWeb Search APIを使い、セキュリティチームが使うOSSパッケージやコンテナイメージの更新を毎朝調べるLangGraphのグラフを構築する。3つのエコシステムを並列に調査し、日付範囲・ブロックリスト・検索予算はモデルが変更できないコード側で保持する。

## 設計のポイント

- 日付窓、ブロックリスト、検索予算をモデルの外で強制する。
- 3つのエコシステムを並列調査する。
- 引用元との照合と既報告の記憶で重複や誤りを減らす。
- AgentCore Gatewayで管理者のソースポリシーを全エージェントに適用する。

## 使いどころ

- 日々変わる脆弱性情報の監視。
- 検索クエリを自社クラウド内に留めたい組織。
