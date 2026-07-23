---
type: guidance
title: '音声エージェントのアーキテクチャ選定: Speech-to-Speech vs チェイン型'
title_original: Voice agents
industry: cross-industry
cloud: []
patterns:
- voice-agent
components:
- RealtimeAgent
- RealtimeSession
- VoicePipeline
- gpt-realtime-2.1
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/voice-agents?voice-agent-architecture=speech-to-speech#speech-to-speech-realtime-architecture
published_at: '2025-07-21'
---

## 概要

OpenAIの音声エージェントガイドは、ライブ音声を直接扱うSpeech-to-Speechアーキテクチャと、音声認識・テキスト推論・音声合成を明示的に連結するチェイン型パイプラインのどちらを選ぶべきかを解説する。自然で低遅延な会話にはRealtimeAgent/RealtimeSessionによるSpeech-to-Speechを、既存テキストエージェントの拡張や中間テキストの制御が必要な場合はVoicePipelineによるチェイン型を推奨する。

## 設計のポイント

- 会話の自然さ・低遅延・バージイン(割り込み)が重要ならSpeech-to-Speechセッションを選ぶ
- 承認フローや文字起こしの永続化など中間ステージの可視性・制御が必要ならチェイン型を選ぶ
- 音声トランスポート層とビジネスロジック(ツール・ハンドオフ・ガードレール)を分離して設計する
- アーキテクチャを先に決めてから、テキストエージェントと同様の設計判断(ツール・オーケストレーション・ガードレール)を進める

## 使いどころ

- カスタマーサポートなど承認や監査ログが必要な音声ワークフロー
- ブラウザでの低遅延な会話型音声アシスタント
- 既存のテキストベースエージェントに音声インターフェースを追加したい場合
