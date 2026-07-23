---
type: guidance
title: 音声エージェント構築のためのRealtime/Audio APIアーキテクチャ選定ガイド
title_original: Build voice agents
industry: cross-industry
cloud: []
patterns:
- voice-agent
- realtime-transcription
- realtime-translation
components:
- gpt-realtime-2.1
- gpt-realtime-translate
- gpt-realtime-whisper
- Realtime API
outcome:
  type: speed
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/realtime
published_at: '2025-07-21'
---

## 概要

音声アプリを構築する際に、低遅延なライブ会話にはRealtimeセッション、ファイルや非ライブの音声処理にはリクエスト型のAudio APIが適するというアーキテクチャ選定の指針を示す。音声エージェント・ライブ翻訳・文字起こし・音声生成という4つの用途ごとに最適なモデルとエンドポイントが整理されている。

## 設計のポイント

- ユースケース（会話/翻訳/文字起こし/音声生成）ごとに専用モデルとセッションタイプが用意されており、目的から逆算してアーキテクチャを選ぶ。
- Realtimeセッションは接続を張り続けてイベントをやり取りするステートフルな設計で、既存のChat Completionsアプリに音声を足す場合は音声対応チャットモデルという選択肢もある。

## 使いどころ

- ブラウザ上でリアルタイムに会話する音声エージェントを新規に設計する場合。
- 既存のテキストベースAIアプリに音声入出力を追加するかどうかを判断する場合。
