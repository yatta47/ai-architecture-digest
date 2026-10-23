---
type: guidance
title: AIエージェントの応答をKokoro TTSで文単位にストリーミングし低遅延化する
title_original: Stream low-latency speech from AI agents using Kokoro TTS on Amazon SageMaker AI
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- voice-agent
- inference-optimization
components:
- Kokoro-82M
- Amazon SageMaker AI
- Amazon Bedrock AgentCore
- ml.g5.xlarge
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/stream-low-latency-speech-from-ai-agents-using-kokoro-tts-on-amazon-sagemaker-ai/
published_at: '2026-10-22'
---

## 概要

音声エージェントの応答全体の生成を待たず、1文ごとにSageMaker上のKokoro-82M(TTS)へ送って合成を始める構成を示す。コンテナはPOSTのストリーミング経路と双方向WebSocket経路を持ち、ブラウザへの2つの配信方式のコスト差も比較する。

## 設計のポイント

- エージェントが文を出し次第TTSに流し、生成と合成を並行させる。
- 82Mパラメータの小型モデルで、1台のGPUインスタンスで低遅延かつ低コストにする。
- 単発ストリーミングと双方向接続を比較し、用途で使い分ける。

## 使いどころ

- 音声エージェントの初回音声までの待ち時間を縮めたいチーム。
- 小型TTSを自前ホスティングしてコストを抑えたい場合。
