---
type: guidance
title: Realtime APIのセッション状態管理とイベントフロー設計
title_original: Realtime conversations
industry: cross-industry
cloud: []
patterns:
- voice-agent
components:
- gpt-realtime-2.1
- Realtime API
outcome:
  type: speed
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/realtime-conversations
published_at: '2025-07-21'
---

## 概要

WebRTCまたはWebSocketで接続したRealtime APIを使い、gpt-realtime-2.1のようなモデルと音声対音声の会話を行うための、セッション・カンバセーション・レスポンスという3つの構成要素とクライアント/サーバーイベントのやり取りを解説する。応答を必要としない場合はtranscriptionモードを使う分岐も示される。

## 設計のポイント

- WebRTCは音声の送受信の多くをAPIが肩代わりするが、WebSocketを使う場合は入力音声バッファを手動でハンドリングする必要がある。
- Session（設定）・Conversation（入出力アイテム）・Response（生成されたアイテム）という3層構造でセッション状態をモデル化する。

## 使いどころ

- ブラウザやサーバーからライブの音声対話を実装する際のイベント設計。
- 応答不要な文字起こし専用ユースケースとの使い分けを判断する場合。
