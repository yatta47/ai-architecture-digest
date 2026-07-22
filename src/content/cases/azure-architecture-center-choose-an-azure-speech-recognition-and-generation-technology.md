---
type: guidance
title: Azureで音声認識・音声合成技術を選定するガイド
title_original: Choose an Azure speech recognition and generation technology
industry: cross-industry
cloud:
- azure
patterns:
- realtime-transcription
- realtime-translation
- voice-agent
- multi-model-routing
components:
- Azure Speech
- Azure OpenAI
- GPT-4o Realtime
- GPT-4o audio
- Voice Live API
- Speech Studio
- Speech SDK
- Speech CLI
- Custom Speech
- Custom Voice
- TTS avatar
- Azure Language
- Azure Translator
- Content Safety
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/data-guide/ai-services/speech-recognition-generation
published_at: '2026-03-24'
---

## 概要

Microsoft Foundry上でSTT/TTSを実装する際、単機能に特化したAzure Speechと、音声を言語理解・生成と統合したいAzure OpenAIオーディオモデル（GPT-4o Realtime/GPT-4o audio）のどちらを使うべきかを比較する意思決定ガイド。用途別（字幕生成、コールセンター文字起こし、発音評価、音声エージェント、アバター動画生成）に適した機能とデプロイ・統合方法を整理している。

## 設計のポイント

- リアルタイム性重視・純粋な音声変換にはAzure Speechのストリーミング型STT/TTSを使い、音声と言語理解・推論・生成を1回のモデル呼び出しで完結させたい場合はAzure OpenAIのオーディオモデルを選ぶという判断基準を設ける。
- 業界特有の専門用語や雑音を含む音声にはCustom Speechで音響・言語モデルを追加学習させ、ベースモデルの精度不足を補う。
- ブランド固有の声が必要な場面ではCustom Voiceで専用音声を構築し、他システムとの差別化を図る。
- ノーコードのSpeech Studio、多言語対応のSpeech SDK、CLI、REST APIの中から開発体制や統合要件に応じて連携方式を選択する。

## 使いどころ

- コールセンターでのリアルタイム/バッチ通話文字起こしと個人情報のマスキング、感情分析による顧客体験改善。
- 配信・動画コンテンツ向けの字幕生成や多言語吹き替え、プロファニティフィルタ適用。
- 語学学習アプリでの発音評価とリアルタイムフィードバック提供。
- チャットボットや音声エージェント（Voice Live API）による自然な音声対話やアバター動画の構築。
