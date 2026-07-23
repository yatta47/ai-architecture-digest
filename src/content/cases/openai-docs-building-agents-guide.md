---
type: guidance
title: Responses APIとAgents SDKの使い分けガイド
title_original: Building agents
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- guardrails
components:
- OpenAI Agents SDK
- Responses API
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/agents
published_at: '2025-07-18'
---

## 概要

OpenAIのエージェント構築ガイドは、モデル呼び出し・ツール・状態・オーケストレーションを自前で制御したい場合はResponses API、エージェントループやハンドオフ、セッション、トレーシング、ガードレールをSDKに任せたい場合はAgents SDKを使うべきという判断基準を示す。

## 設計のポイント

- カスタムのツールルーティングやループを自分で実装したいならResponses APIの関数呼び出しフローを直接使う
- 複数の専門エージェントへの委譲や繰り返しツール呼び出しが多いワークフローはAgents SDKのランナーに任せる
- ガードレール・トレーシング・resumableな承認フローが必要ならAgents SDKの組み込み機能を活用する

## 使いどころ

- カスタムの状態管理やモデル呼び出し制御が必要なプロダクトへのAI機能組み込み
- 複数専門エージェントへのルーティングと承認フローが必要な業務システム
