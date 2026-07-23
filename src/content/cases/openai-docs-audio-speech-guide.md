---
type: guidance
title: 'OpenAI音声アーキテクチャ全体像: リクエスト型 vs リアルタイムセッション'
title_original: Audio and speech
industry: cross-industry
cloud: []
patterns:
- voice-agent
- realtime-transcription
- realtime-translation
components:
- gpt-realtime-2.1
- gpt-audio-1.5
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/audio
published_at: '2025-07-21'
---

## 概要

OpenAIの音声ガイドは、音声入力・音声出力・テキスト文字起こし・テキストプロンプトという4つのモダリティと、リクエストベースAPI・リアルタイムセッション・マルチモーダルチャットという3つのアーキテクチャの使い分けを整理する。ファイルや境界のあるリクエストにはSpeech-to-Text/Text-to-Speech、ライブで低遅延なやり取りにはRealtimeセッションを推奨する。

## 設計のポイント

- ユースケース(ファイル処理かライブ対話か)に応じてリクエストベースAPIかリアルタイムセッションかを最初に選ぶ
- 既存のChat Completionsベースのテキストエージェントには、modalitiesにaudioを追加するだけで音声入出力を拡張できる
- ブラウザ音声エージェントはWebRTC経由のRealtimeSessionを使い、サーバー側で発行した短命キーで接続する

## 使いどころ

- 既存のテキストチャットアプリに音声入出力を後付けしたい場合
- 字幕・通話分析・検索用途などテキスト文字起こしが必要な場面
- 低遅延な音声対話エージェントを新規に構築する場合
