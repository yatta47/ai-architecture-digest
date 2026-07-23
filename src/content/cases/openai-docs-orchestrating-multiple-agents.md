---
type: guidance
title: LLMによる自律オーケストレーションとコードによる制御を組み合わせるマルチエージェント設計
title_original: Orchestrating multiple agents
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
components:
- OpenAI Agents SDK
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://openai.github.io/openai-agents-python/multi_agent/
published_at: '2025-07-21'
---

## 概要

エージェントのオーケストレーションを、LLM自身に計画・意思決定させる方式と、コードでフローを決定する方式の2つに整理し、両者を組み合わせられるとする。Agents SDKでは『マネージャーエージェントが専門エージェントをツールとして呼ぶ（Agents as tools）』と『複数エージェントが会話を引き継ぐハンドオフ』という2つの中心的パターンが解説される。

## 設計のポイント

- 最終回答の一元管理やガードレールの一括適用が必要ならAgents as toolsパターン、専門エージェント間で会話ごと引き継ぐならハンドオフパターンを選ぶ。
- Web検索・ファイル検索・コード実行・コンピュータ操作といったツールと専門エージェントへのハンドオフを組み合わせることで、開放的なタスクを自律的に計画・実行させられる。

## 使いどころ

- リサーチや計画立案など、複数の専門性を組み合わせる必要があるオープンエンドなタスクを自動化したい場合。
- 1つのエージェントに任せるには複雑すぎるワークフローを、責務ごとに複数エージェントへ分割したい場合。
