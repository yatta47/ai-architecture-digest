---
type: guidance
title: 推論する音声エージェントのプロンプト設計ガイド（gpt-realtime-2）
title_original: Realtime 2.0 Prompting Guide (Realtime Models Prompting)
industry: cross-industry
cloud: []
patterns:
- voice-agent
- prompt-optimization
- context-engineering
- ai-agent
components:
- gpt-realtime-2
- gpt-realtime-1.5
- OpenAI Realtime API
data_sources:
- 音声入力
- ツール呼び出し
- 長時間セッションの状態
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/realtime-models-prompting
published_at: '2026-05-05'
---

## 概要

OpenAIの低遅延な音声対話モデル gpt-realtime-2 向けのプロンプト設計ガイド。「話す前に考える」内部推論・ツール呼び出し・128kトークンの長文コンテキストを活かすため、アシスタントの責務・判断点・ツール方針・ガードレールを明確に定義する方法を示す。最初から作り込まず最小限のプロンプトで始め、評価で失敗した挙動にだけ指示を追加することを推奨している。

## 設計のポイント

「be helpful」のような曖昧な指示を避け、いつ・何を・いつやらないかをトリガー/アクション/例外ルールで記述する。推論の深さ(reasoning.effort)は minimal〜xhigh の5段階でタスク複雑度・遅延許容度・失敗コストから選び、多くの本番音声エージェントは low から始める。プリアンブル（作業中を伝える短い口頭の進捗更新）や書き込み前の確認境界を明示的に制御し、# Role / # Reasoning / # Preambles などラベル付きの短い節でプロンプトを構造化して、モデルが該当指示を素早く見つけられるようにする。

## 使いどころ

- カスタマーサポートや注文・予約照会、技術サポートなど、ツール連携と長時間セッションを伴う音声エージェントを設計・チューニングする開発者に有効
- 遅延と推論の深さのトレードオフを制御したい場面で特に有効
