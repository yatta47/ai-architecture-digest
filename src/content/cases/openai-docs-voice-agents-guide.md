---
type: guidance
title: 低遅延なspeech-to-speechと制御しやすいchained方式、音声エージェントの2大構成
title_original: Voice agents guide
industry: cross-industry
cloud: []
patterns:
- voice-agent
components:
- RealtimeAgent
- RealtimeSession
- VoicePipeline
- Agents SDK
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/voice-agents
published_at: '2025-07-18'
---

## 概要

音声エージェントの設計は、モデルがライブ音声を直接扱うspeech-to-speech方式と、音声認識→テキスト推論→音声合成を明示的に連結するchained方式のどちらを選ぶかが最初の分岐点になる。前者は自然な低遅延の会話に強く、後者は既存テキストエージェントの再利用や承認フローの挿入がしやすい。

## 設計のポイント

- 自然な割り込み・低遅延な会話が必要ならRealtimeAgent/RealtimeSessionによるspeech-to-speech方式を選ぶ。
- 文字起こしを保持したい、既存のテキストエージェントを流用したい、各段階に承認・ポリシーチェックを挟みたい場合はchained VoicePipelineを選ぶ。
- どちらの方式でもツール・ハンドオフ・ガードレールといったエージェントの中核設計はテキストエージェントと共通の考え方を適用する。

## 使いどころ

- 低遅延な音声対話体験を最優先するコンシューマー向け音声アシスタント。
- 承認ステップや文字起こし保存が必須のサポート業務・規制対応が絡む音声フロー。
