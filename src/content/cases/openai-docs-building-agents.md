---
type: guidance
title: 指示・ガードレール・ツールの3要素でエージェントを定義するビルディングトラック
title_original: Building agents
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
components:
- Responses API
- Agents SDK
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/tracks/building-agents/
published_at: '2025-07-11'
---

## 概要

OpenAIのエージェント構築ラーニングトラックは、エージェントを『指示(すべきこと)・ガードレール(すべきでないこと)・ツール(できること)を持ち、ユーザーに代わって行動するAIシステム』と定義し、モデル選定・ツール活用・オーケストレーションという核となる構成要素を整理する。

## 設計のポイント

- 単に質問に答えるだけのチャットボットと、外部システムに接続して行動を起こすエージェントを明確に区別して設計判断の起点にする。
- 推論モデルは計画・数学・コード生成・複数ツールにまたがる複雑タスクに、非推論モデルは対話性重視の低遅延タスクに使うという判断基準を提示する。
- Responses APIで自前にロジックを組むか、抽象度の高いAgents SDKでマルチエージェント連携を素早く組むかを、制御の細かさとのトレードオフで選ばせる。

## 使いどころ

- 初めてエージェントを設計する開発者が、モデル選定からツール設計まで一気通貫で学びたい場合。
- Responses APIとAgents SDKのどちらを軸に実装すべきか判断材料が欲しい場合。
