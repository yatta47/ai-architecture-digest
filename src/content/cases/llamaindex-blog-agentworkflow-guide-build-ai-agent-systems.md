---
type: announcement
title: 複数エージェントの状態管理とオーケストレーションを担うAgentWorkflow
title_original: 'Introducing AgentWorkflow: A Powerful System for Building AI Agent Systems'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- context-engineering
- human-in-the-loop
components:
- LlamaIndex Workflows
- AgentWorkflow
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-agentworkflow-a-powerful-system-for-building-ai-agent-systems
published_at: '2026-07-19'
---

## 概要

LlamaIndexが既存のWorkflow抽象の上に構築した新機能AgentWorkflowを発表。単一エージェントから複数エージェントの協調まで、状態管理・リアルタイム可視化・Human-in-the-Loopを備えたシステムを少ないボイラープレートで構築できるようにする。

## 設計のポイント

- Workflowの上にAgentWorkflowを重ね、エージェント間の調停・状態保持のボイラープレートを抽象化する
- 単一エージェント構成から複数エージェント協調構成まで同一APIでスケールさせる
- 実行中のエージェント活動をリアルタイムにストリーミング・監視できるようにする

## 使いどころ

- リサーチアシスタントのように複数ソースの調査・統合・レビューを要するエージェントシステムの構築
- エージェント間のハンドオフや状態管理が複雑化してきたチームの実装簡素化
