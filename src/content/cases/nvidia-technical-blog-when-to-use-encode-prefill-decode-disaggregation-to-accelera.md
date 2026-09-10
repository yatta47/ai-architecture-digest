---
type: guidance
title: マルチモーダル推論を高速化するEncode-Prefill-Decode分離の使いどころ
title_original: When to Use Encode-Prefill-Decode Disaggregation to Accelerate Multimodal Model Serving
industry: cross-industry
cloud: []
patterns:
- inference-optimization
components:
- NVIDIA Dynamo
- NIXL
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/
published_at: '2026-09-09'
---

## 概要

NVIDIA Dynamoは、マルチモーダル推論のビジョンエンコード段階をLLMのprefill/decodeから分離するEPD（Encode-Prefill-Decode）分離により、画像主体で出力が短中程度、量子化MoEモデルのケースで最大5倍速いTTFTと7倍速いエンドツーエンド応答を実現する。テキストと画像の混在トラフィックではヘッドオブラインブロッキングを解消し、テキストのTTFTを42.2%削減する一方、decode支配的なワークロードでは効果が薄れる条件も明示する。

## 設計のポイント

- ビジョンエンコーダを独立したワーカー群として切り出し、prefill/decodeと別スケジューリングドメインでスケールさせる
- GPUコロケーション・完全分離など複数のエンコーダ配置トポロジーから、入力メディア量や出力長に応じて選択する
- ビジョンエンコーダをBF16のまま維持しLLM側だけNVFP4量子化するなど、コンポーネントごとに異なる精度戦略を採る

## 使いどころ

- 画像や動画を多く含むプロンプトを扱うマルチモーダルAIサービスのレイテンシ改善
- テキストのみのリクエストと画像混在リクエストが同居し、ヘッドオブラインブロッキングが発生している推論基盤
