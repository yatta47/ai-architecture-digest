---
type: case
title: WorkdayのLangGraph/LangSmithによる社内エージェント基盤
title_original: How Workday Built an Enterprise-Scale AI Agent Platform with LangGraph and LangSmith
company: Workday
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llm-gateway
- rag
- eval
components:
- LangGraph
- LangSmith
- LangChain
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-workday-built-an-enterprise-scale-ai-agent-platform-with-langgraph-and-langsmith
published_at: '2026-11-10'
---

## 概要

Workdayは4人のチームで、LangGraphによるオーケストレーションとLangSmithによる観測・評価を使った社内エージェント基盤を構築した。LangChainを包むSDKでLLMゲートウェイやRAGなどを経由させ、エージェントが使えるAPIを統制するAgent System of Recordも提供する。

## 設計のポイント

- SDKでLLMゲートウェイやRAG等の社内サービスに統一的に接続する。
- エージェントがアクセスできるAPIを統制層で管理する。
- 評価基盤を共有化して品質確認を行う。

## 使いどころ

- 厳格な監査要件下で社内向けエージェント基盤を作る企業
