---
type: announcement
title: 60言語対応・低遅延を両立した音声認識モデルMAI-Transcribe-2
title_original: MAI-Transcribe-2 is the fastest, most accurate and cheapest speech recognition model in the world
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- realtime-transcription
- multilingual-localization
- inference-optimization
components:
- MAI-Transcribe-2
- Microsoft Foundry
- MAI Playground
- Open Router
outcome:
  type: speed
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://microsoft.ai/news/mai-transcribe-2-is-the-fastest-most-accurate-and-cheapest-speech-recognition-model-in-the-world/
published_at: '2026-09-03'
---

## 概要

Microsoftが音声認識モデルMAI-Transcribe-2を発表。話者分離・単語単位のタイムスタンプ・キーワードバイアス・言語コードスイッチングに対応し、FLEURSベンチマーク60言語で高精度かつ主要競合より最大10倍高速、1時間0.10ドルという低価格を実現した。

## 設計のポイント

- 精度とレイテンシのパレートフロンティアを追求し、長尺音声でも高速処理できるよう最適化する
- verbatim/cleanなど出力スタイルを切り替え可能にし、コンプライアンス用途と可読性重視の字幕用途を1モデルで両立する
- 自動言語識別とコードスイッチング対応により多言語環境で単一モデル運用を可能にしコスト・運用複雑性を下げる

## 使いどころ

- 臨床記録や法務文書など高精度な文字起こしが必要な業務
- 字幕生成やアクセシビリティ対応でのリアルタイム/バッチ文字起こし
- 多言語混在の会話が発生するグローバル企業のコールセンターや会議記録
