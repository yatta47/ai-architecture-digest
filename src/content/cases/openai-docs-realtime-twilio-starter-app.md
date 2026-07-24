---
type: guidance
title: TwilioとRealtime APIを橋渡しする電話音声アシスタントの最小構成
title_original: OpenAI Realtime API with Twilio Quickstart
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- voice-agent
components:
- Realtime API
- Twilio
- ngrok
- WebSocket
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-realtime-twilio-demo
published_at: '2025-07-18'
---

## 概要

OpenAIのRealtime API×Twilio Quickstartは、TwiMLでTwilioの着信を双方向ストリームとしてWebSocketバックエンドに渡し、そこからRealtime APIへ転送することで電話経由の音声AIアシスタントを構築するリファレンス実装。webapp(設定・文字起こし表示用)とwebsocket-server(Twilio-Realtime間の中継)の2アプリ構成。

## 設計のポイント

- TwiMLの<Stream>で着信をWebSocketの双方向ストリームに変換し、Twilio・Realtime API・フロントエンドの3者間でメッセージを中継する構成にする。
- ローカル開発時はngrokで一時的に外部公開し、Twilio Webhookの到達性を確保する。
- 本番セキュリティ対策は最小限である旨を明記し、実運用前に監査を必須とする注意書きを添える。

## 使いどころ

- 既存の電話番号にAI音声アシスタントを接続するプロトタイプを素早く立ち上げたい場合。
