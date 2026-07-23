---
type: guidance
title: OpenAI音声翻訳API(音声→英語テキスト翻訳)ガイド
title_original: 'Speech to text: Translations'
industry: cross-industry
cloud: []
patterns:
- realtime-translation
components:
- Whisper
- gpt-4o-transcribe
- gpt-4o-mini-transcribe
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/speech-to-text#translations
published_at: '2025-07-21'
---

## 概要

OpenAIのAudio APIのtranslationsエンドポイントは、任意言語の音声を英語のテキストへ翻訳・文字起こしする。Whisperベースのモデルに加え、gpt-4o-transcribe系の高品質モデルが文字起こし用途で利用可能で、ファイルアップロードは25MBまでmp3/mp4/wav等の形式に対応する。

## 設計のポイント

- 音声を元言語のまま文字起こしする用途と、英語へ翻訳して出力する用途を同じAudio API系列で使い分けられる
- ファイルベースの境界リクエストにはtranslations/transcriptions、ライブストリームにはRealtime transcriptionを使う

## 使いどころ

- 非英語音声コンテンツを英語字幕・議事録に変換したい多言語コンテンツ運用
- グローバルなカスタマーサポート通話を英語で一元的にログ化したい場合
