---
type: guidance
title: 音声対話でFunction Callingを叩き3Dシーンを操作する太陽系デモ
title_original: Realtime Solar System Demo
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- voice-agent
components:
- Realtime API
- WebRTC
- Spline
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-realtime-solar-system
published_at: '2025-07-18'
---

## 概要

Realtime Solar System Demoは、OpenAI Realtime API(WebRTC)による音声対話からFunction Callingで3Dシーン(Spline製太陽系モデル)のアニメーションやチャート表示を駆動する実装例。惑星や衛星について話しかけると、対応するトリガーが呼ばれてカメラワークやビジュアルが変化する。

## 設計のポイント

- 会話内容をトリガーとするfunction callをSplineシーンのmouseDown等のイベント発火にマッピングし、音声対話とビジュアル演出を疎結合につなぐ。
- データに基づく質問(惑星の水陸比率など)にはグラフ描画のトリガーを用意し、音声応答だけでなく視覚的な回答も返せるようにする。

## 使いどころ

- 音声エージェントのfunction callingでリッチな3D/2Dビジュアルを操作する体験を設計したい場合。
