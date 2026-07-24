---
type: guidance
title: WebRTC経由のRealtime APIイベントを可視化する検証用コンソール実装
title_original: OpenAI Realtime Console
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- voice-agent
components:
- Realtime API
- WebRTC
- React
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-realtime-console
published_at: '2025-07-18'
---

## 概要

OpenAI Realtime ConsoleはRealtime APIをWebRTCで利用する最小構成のリファレンス実装で、Expressサーバーがビルド済みReactフロントエンドを配信し、クライアント/サーバー双方のイベントJSONペイロードをログパネルで確認しながらクライアントサイドのfunction callingを設定できる。

## 設計のポイント

- WebRTCデータチャネル経由でRealtime APIのイベント送受信を行う最小構成にすることで、統合の全体像を素早く把握できるようにする。
- イベントログパネルをUIに組み込み、client/server双方のJSONペイロードをその場で確認できるようにしてデバッグを容易にする。

## 使いどころ

- Realtime APIのWebRTC統合を最初に試作し、イベントの流れを理解したい開発者。
