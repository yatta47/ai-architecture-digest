---
type: guidance
title: 社内コーディングAgent向けOSSフレームワークOpen SWE
title_original: 'Open SWE: An open-source framework for internal coding agents'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- context-engineering
components:
- Open SWE
- Deep Agents
- LangGraph
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/open-swe-an-open-source-framework-for-internal-coding-agents
published_at: '2026-10-13'
---

## 概要

Stripe・Ramp・Coinbaseの社内コーディングAgentが収束した設計(隔離サンドボックス、厳選ツール、Slack起点、起動時の文脈取得、サブエージェント)をOSSとして実装したのがOpen SWEである。

## 設計のポイント

- タスクごとに隔離したクラウドサンドボックスで被害範囲を限定する。
- ツールは数より厳選・保守を重視する。
- Linear/Slack/PRの文脈を起動時に取り込む。
- 複雑なタスクは文脈分離したサブエージェントに委譲する。

## 使いどころ

- 社内コーディングAgentを立ち上げる組織の出発点。
