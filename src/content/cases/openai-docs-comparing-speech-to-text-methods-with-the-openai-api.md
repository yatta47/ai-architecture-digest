---
type: guidance
title: OpenAI APIによる音声認識(STT)手法の比較ガイド
title_original: Comparing Speech-to-Text Methods with the OpenAI API
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- realtime-transcription
- voice-agent
components:
- OpenAI API
- gpt-4o-transcribe
- Realtime API
- Agents SDK VoicePipeline
- WebSockets
- WebRTC
outcome:
  type: speed
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/speech_transcription_methods/
published_at: '2025-04-29'
---

## 概要

OpenAIのcookbookが、ファイル一括アップロード、ストリーミングアップロード、Realtime WebSocket、Agents SDKのVoicePipelineという4つの音声文字起こし(STT)手法をレイテンシ・ユースケース・利点/制約の観点で比較している。gpt-4o-transcribeモデルを使い、ボイスメール処理からライブキャプション、社内ヘルプデスクのエージェント構築まで、適した手法を選べるようにする実践ガイドになっている。

## 設計のポイント

- レイテンシ要件（バッチ処理か、準リアルタイムか、真のリアルタイムか）に応じてFile upload(blocking)/streaming/Realtime WebSocket/Agents SDKの4手法を使い分ける。
- Realtime WebSocketはpcm16/g711_ulaw/g711_alawの音声形式のみに対応し、セッションは最大30分で再接続・結合処理が必要になる点を設計に織り込む。
- Agents SDKのVoicePipelineを使うとエージェント的な音声ワークフローを比較的簡単に構築できるが、Python限定かつベータでAPIが変わりうる。

## 使いどころ

- ボイスメールやコールセンター録音などバッチ処理でよい用途にはシンプルなファイルアップロード方式が向く。
- モバイルアプリのボイスメモのように『生きている感』を出したいUIにはストリーミングレスポンスが有効。
- ウェビナーのライブキャプションのような真のリアルタイム字幕にはRealtime WebSocketが必須。
- 社内ヘルプデスクのような音声対話エージェントを構築する場合はAgents SDKのVoicePipelineが適する。
