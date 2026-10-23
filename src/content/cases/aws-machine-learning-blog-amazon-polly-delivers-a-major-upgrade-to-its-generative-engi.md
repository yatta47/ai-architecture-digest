---
type: announcement
title: Amazon Polly Generativeエンジンの音声品質向上と新ボイス追加
title_original: Amazon Polly delivers a major upgrade to its Generative engine
company: AWS
industry: media
cloud:
- aws
patterns:
- voice-agent
components:
- Amazon Polly
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-polly-delivers-a-major-upgrade-to-its-generative-engine/
published_at: '2026-10-22'
---

## 概要

Amazon PollyのGenerativeエンジンがアップグレードされ、表現力と数字・住所などの読み上げ精度が向上した。9ロケールに14ボイスが追加され、ヒンディー語とフィンランド語が初めて一般提供となる。既存アプリはAPI変更なしで利用できる。

## 設計のポイント

- ボイス名とAPI呼び出しを変えないドロップイン更新にしている。
- 数字・通貨・住所の読み上げ精度を、コンタクトセンターやエージェント用途の要件として改善している。

## 使いどころ

- 音声エージェントやコンタクトセンターのTTS品質を上げたい開発者。
- 多言語の音声出力が必要なサービス。
