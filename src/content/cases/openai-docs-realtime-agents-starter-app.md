---
type: guidance
title: 軽量リアルタイムエージェント+高性能supervisorで音声応答の質と速度を両立
title_original: Realtime API Agents Demo
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- voice-agent
- multi-agent-orchestration
components:
- Realtime API
- Agents SDK
- gpt-4.1
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-realtime-agents
published_at: '2025-07-18'
---

## 概要

OpenAI Realtime Agents Demoは、音声対話を担う軽量なリアルタイムエージェントが基本応答を返しつつ、複雑なツール呼び出しや高度な応答をテキストベースの上位supervisorモデル(gpt-4.1)に委譲するChat-Supervisorパターンと、専門特化したリアルタイムエージェント間でユーザーを引き継ぐSequential Handoffパターンの2つのマルチエージェント構成を示す。

## 設計のポイント

- 簡単な会話や情報収集は軽量realtimeモデルが即答し、複雑な判断やツール呼び出しだけを高性能supervisorモデルに委譲することで、応答速度と精度のトレードオフを両立する。
- 既存のテキストエージェントのプロンプト・ツールをsupervisorにそのまま流用でき、テキストエージェントから音声エージェントへの移行コストを抑えられる。
- カスタマーサポートのように意図ごとに専門エージェントを用意し、Sequential Handoffで順番に引き継ぐことで、単一エージェントに指示とツールを詰め込みすぎて性能が劣化するのを防ぐ。

## 使いどころ

- 既にテキストの高性能エージェントを持っていて、それを段階的に音声対応させたいチーム。
- カスタマーサポートなど意図ごとに専門エージェントを分けたいマルチエージェント音声システム。
