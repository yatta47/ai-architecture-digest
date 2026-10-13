---
type: announcement
title: ScaleDownの制約付きデコードモデルで長時間エージェントの文脈管理
title_original: Building long-running agents with ScaleDown and Deep Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- context-engineering
- cost-optimization
- llm-gateway
components:
- ScaleDown
- langchain-scaledown
- LangSmith LLM Gateway
- Deep Agents
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/building-long-running-agents-with-scaledown-and-deep-agents
published_at: '2026-10-13'
---

## 概要

要約・圧縮・抽出・分類の各タスク専用の制約付きデコードモデルを文脈管理に使うミドルウェアを提供し、フロンティアモデルより高速・安価に履歴要約やツール結果圧縮を行う。

## 設計のポイント

- 文脈管理の判断を小型専用モデルに切り出す。
- 要約・圧縮・抽出をミドルウェアでエージェントループに差し込む。

## 使いどころ

- 長時間稼働エージェントの文脈管理コストを下げたい場面。
