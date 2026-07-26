---
type: guidance
title: 実況音声からポッドキャストを自動生成するマルチモーダル生成AIパイプライン
title_original: 'Generative AI use case: Generate podcasts from audio files'
industry: media
cloud:
- gcp
patterns:
- document-processing
- human-in-the-loop
components:
- Speech-to-Text
- Text-to-Speech
- Gemini API
- Cloud Storage
- Cloud Run
- Eventarc
outcome:
  type: productivity
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/genai-podcasts-from-commentary
published_at: '2026-07-19'
---

## 概要

スポーツ実況などの音声ファイルをSpeech-to-Textでタイムスタンプ付き文字起こしにし、Gemini APIがポッドキャスト台本を生成、人間の校閲を経てText-to-Speechで音声化するメディア向けパイプライン。音声入力から音声出力までを生成AIで一気通貫に処理する。

## 設計のポイント

- Eventarcで音声アップロードをトリガーにCloud Runで処理を自動起動し、文字起こし→台本生成の流れをつなぐ
- 生成した台本ドラフトを配信前に人間がレビュー・編集するステップを明示的に組み込んでいる
- Speech-to-TextとText-to-Speechという入出力の異なるマルチモーダルAPIをGemini APIの前後に配置して一連のパイプライン化している

## 使いどころ

- スポーツ実況やイベント音源から要約コンテンツを大量生産したいメディア企業
- 音声素材をテキスト経由で別フォーマットのコンテンツに再編集したいコンテンツ制作チーム
