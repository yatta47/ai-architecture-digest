---
type: guidance
title: OpenAI音声認識APIの文字起こし・話者分離ガイド
title_original: 'Speech to text: Transcriptions'
industry: cross-industry
cloud: []
patterns:
- realtime-transcription
components:
- gpt-4o-transcribe
- gpt-4o-mini-transcribe
- gpt-4o-transcribe-diarize
- Whisper
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/speech-to-text#transcriptions
published_at: '2025-07-21'
---

## 概要

OpenAIのAudio APIは、Whisperベースのモデルに加えgpt-4o-transcribe系の高品質モデルによる音声文字起こしをサポートする。話者分離モデルgpt-4o-transcribe-diarizeでは既知話者の参照クリップを与えることで話者ラベル付きの文字起こしが可能で、ストリーミング時はセグメント単位でイベントが発火する。

## 設計のポイント

- ファイルアップロード・境界のある音声にはtranscriptions API、ライブ音声にはRealtime transcriptionを使い分ける
- gpt-4o-transcribe-diarizeでは30秒超の音声にchunking_strategyの指定が必須になる制約を踏まえて設計する
- known_speaker_references[]に2〜10秒の参照クリップを与えることで既知話者にセグメントをマッピングできる

## 使いどころ

- 会議録音やコールセンター通話を話者ラベル付きで文字起こししたい場合
- 字幕・議事録・検索用途などバッチ処理向けの音声文字起こし
- マイクやメディアストリームからのライブ文字起こしが必要なリアルタイムアプリ
