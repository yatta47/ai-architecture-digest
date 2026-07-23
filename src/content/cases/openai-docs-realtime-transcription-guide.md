---
type: guidance
title: gpt-realtime-whisperによるライブ文字起こしセッションの設計
title_original: Realtime transcription
industry: cross-industry
cloud: []
patterns:
- realtime-transcription
components:
- gpt-realtime-whisper
- gpt-4o-transcribe
- gpt-4o-mini-transcribe
- whisper-1
outcome:
  type: speed
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/realtime-transcription
published_at: '2025-07-21'
---

## 概要

応答を生成しない純粋なライブ音声認識には、type: "transcription"のRealtimeセッションを使い、音声が届く端からトランスクリプトのデルタをストリーミングできる。最低レイテンシが必要ならgpt-realtime-whisper、ストリーミング不要な高精度用途にはgpt-4o-transcribe、低コスト重視ならgpt-4o-mini-transcribeを使い分ける。

## 設計のポイント

- 用途に応じてgpt-realtime-whisper（低遅延ストリーミング）、gpt-4o-transcribe（高精度）、gpt-4o-mini-transcribe（低コスト）をモデル選定基準として使い分ける。
- WebSocketはサーバー側音声パイプライン、WebRTCはブラウザ音声向けと接続方式を用途別に選択する。
- 本番トラフィック切り替え前に自社の音声・言語・語彙・レイテンシ要件で実測評価することを推奨している。

## 使いどころ

- コールセンターや会議ツールでのライブ字幕・文字起こし機能。
- アシスタント応答が不要な純粋な音声入力のテキスト化パイプライン。
