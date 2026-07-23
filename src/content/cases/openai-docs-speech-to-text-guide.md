---
type: guidance
title: Audio APIのtranscriptions/translationsエンドポイントとモデル選定
title_original: Speech to text
industry: cross-industry
cloud: []
patterns:
- audio-transcription
components:
- whisper-1
- gpt-4o-transcribe
- gpt-4o-mini-transcribe
- gpt-4o-transcribe-diarize
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/speech-to-text
published_at: '2025-07-21'
---

## 概要

Audio APIはtranscriptions（文字起こし）とtranslations（英語への翻訳文字起こし）という2つのエンドポイントを提供し、従来のwhisper-1に加えgpt-4o-transcribe系の高品質スナップショットモデルを利用できる。ファイルは25MBまで、対応形式やdiarization（話者分離）の可否などモデルごとの出力フォーマットの違いを整理する。

## 設計のポイント

- ライブのマイク入力やストリームにはRealtime transcriptionを使い、ファイルアップロードや非ライブのリクエストにはこのAudio APIを使うという明確な使い分けがある。
- 話者分離が必要な場合はgpt-4o-transcribe-diarizeを選び、diarized_json形式で話者セグメント付きの結果を得る。
- コストと精度のトレードオフに応じてwhisper-1／gpt-4o-transcribe／gpt-4o-mini-transcribeを選定する。

## 使いどころ

- 会議録音やポッドキャストなど事後処理でよいバッチ文字起こし。
- 複数話者の音声から話者ごとに発言を分離したい議事録作成。
