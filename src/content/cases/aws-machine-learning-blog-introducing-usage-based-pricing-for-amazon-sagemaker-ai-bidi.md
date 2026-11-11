---
type: announcement
title: SageMaker AI双方向ストリーミングの使用量ベース課金（Deepgram対応）
title_original: Introducing usage-based pricing for Amazon SageMaker AI bidirectional streaming
company: Deepgram
industry: cross-industry
cloud:
- aws
patterns:
- voice-agent
- realtime-transcription
- inference-optimization
components:
- Amazon SageMaker AI
- AWS Marketplace
- Deepgram
- WebSocket
outcome:
  type: revenue
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-usage-based-pricing-for-amazon-sagemaker-ai-bidirectional-streaming/
published_at: '2026-11-11'
---

## 概要

SageMaker AIの双方向ストリーミング推論で、モデル提供者がセッション中の実使用量をAWS Marketplaceへ報告できる使用量ベース課金が始まった。推論ストリームと並行する計測専用のWebSocket（メタデータ接続）で使用量を送る方式で、Deepgramが初期パートナーとしてSTT/TTS課金に対応する。

## 設計のポイント

- レスポンスヘッダーでは終了まで総量が分からないため、計測専用の第2のWebSocketを併設する。
- モデルサーバーは対応ヘッダーを返すことでオプトインする。
- Request-Idで計測レコードと推論セッションを突き合わせる。
- 使用量は発生に応じて増分送信するのが推奨。

## 使いどころ

- リアルタイム音声AIをMarketplaceで従量課金提供するモデル提供者。
- 長さが一定でないストリーミング推論の課金設計。
