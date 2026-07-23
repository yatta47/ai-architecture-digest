---
type: guidance
title: gpt-realtime-translateで話者の発話をリアルタイム通訳するセッション設計
title_original: Realtime translation
industry: cross-industry
cloud: []
patterns:
- realtime-translation
components:
- gpt-realtime-translate
- gpt-realtime-2.1
- Realtime API
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/realtime-translation
published_at: '2025-07-21'
---

## 概要

Realtime translationは専用の/v1/realtime/translationsエンドポイントに音声を流し込み、話者が話している間に翻訳音声とトランスクリプトデルタを受け取れる仕組みで、ライブ通訳・多言語通話・放送・会議・レッスンなどに向く。ツール呼び出しや会話管理を行うアシスタントが必要な場合はgpt-realtime-2.1による通常のRealtimeセッションを使う。

## 設計のポイント

- 翻訳セッションはresponse.createを呼ばず音声ストリーム自体から翻訳が開始する、通常の音声エージェントセッションとは異なるライフサイクルを持つ。
- ブラウザ音声にはWebRTC、サーバーが生音声を受け取る構成にはWebSocketを使うというトランスポート選定基準がある。
- 発話の合間の無音も含めて音声を送り続ける必要がある。

## 使いどころ

- 複数言語が混在する会議やイベントのライブ通訳字幕・音声。
- コールセンターやビデオルームでの多言語間リアルタイム通話。
