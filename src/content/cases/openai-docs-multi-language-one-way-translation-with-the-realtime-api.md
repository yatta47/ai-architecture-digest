---
type: guidance
title: OpenAI Realtime APIによる多言語一方向音声翻訳アプリ
title_original: Multi-Language One-Way Translation with the Realtime API
industry: cross-industry
cloud: []
patterns:
- realtime-translation
- voice-agent
components:
- OpenAI Realtime API
- GPT-4o Realtime
- GPT-4o mini Realtime
- WebSockets
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/voice_solutions/one_way_translation_using_realtime_api/
published_at: '2025-03-24'
---

## 概要

OpenAIのRealtime APIとWebSocketsを使い、話者の音声をリアルタイムに複数言語へ翻訳して配信するスピーカー/リスナーアプリのアーキテクチャを解説する。生音声を直接モデルに入力することで、感情やトーン、間などのプロソディを保持したまま翻訳できる点が特徴である。

## 設計のポイント

- 言語ごとに専用のRealtimeセッション（クライアント）を用意し、単一の音声入力を各言語ストリームにフォークして送る
- STT→TTSのカスケード構成ではなく生音声を直接モデルに入力することでプロソディの劣化を防ぐ
- few-shotプロンプトで応答ではなく翻訳のみを返すようモデルを誘導する

## 使いどころ

- 国際会議やカンファレンスでの多言語同時通訳の提供
- リスナーが好きな言語を選んで聞けるライブ配信・イベントの音声翻訳
