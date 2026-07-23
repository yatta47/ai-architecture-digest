---
type: guidance
title: Realtime音声エージェントにおけるツール委譲とセッション音声ハンドリング設計
title_original: Building Voice Agents
industry: cross-industry
cloud: []
patterns:
- voice-agent
- ai-agent
components:
- RealtimeAgent
- RealtimeSession
- OpenAI Agents SDK (JS)
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://openai.github.io/openai-agents-js/guides/voice-agents/build/#delegation-through-tools
published_at: '2025-07-21'
---

## 概要

JS版Agents SDKのRealtimeAgent/RealtimeSessionを使った音声エージェント構築で、トランスポート層ごとに異なる音声ハンドリングの責務（WebRTCは自動、WebSocketは手動）と、ツールへの処理委譲によるセッション構成方法を解説する。session.mutedやsession.mute()によるマイクミュートなど、トランスポートごとの機能差にも注意が必要。

## 設計のポイント

- OpenAIRealtimeWebRTCは音声入出力を自動処理するが、OpenAIRealtimeWebSocketではsendAudio()などで音声データを自前でハンドリングする必要がある。
- ミュート機能はトランスポートによって対応状況が異なり（WebSocketは非対応）、対応していない場合はアプリ側でキャプチャを一時停止する設計にする。
- セッション設定はmodelオプションとconfigオブジェクトで行い、認証やエンドポイントなど接続時の関心事はconnect()に分離する。

## 使いどころ

- ブラウザ・サーバー双方で音声エージェントを実装する際のトランスポート選定と音声ハンドリング設計。
- 音声エージェントに外部ツールの実行を委譲したいアプリケーション。
