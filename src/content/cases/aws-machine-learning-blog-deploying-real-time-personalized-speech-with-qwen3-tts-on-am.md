---
type: guidance
title: JumpStartでQwen3-TTSの音声クローンをリアルタイム配信
title_original: Deploying real-time personalized speech with Qwen3-TTS on Amazon SageMaker AI
company: AWS
industry: media
cloud:
- aws
patterns:
- inference-optimization
- voice-agent
- multilingual-localization
components:
- Amazon SageMaker AI
- Amazon SageMaker JumpStart
- Qwen3-TTS
- vLLM-Omni
- Amazon CloudWatch
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/deploying-real-time-personalized-speech-with-qwen3-tts-on-amazon-sagemaker-ai/
published_at: '2026-09-25'
---

## 概要

Qwen3-TTS-12Hz-1.7B-BaseをSageMaker JumpStartからリアルタイムエンドポイントへデプロイし、短い参照音声から話者の声で合成する手順を示す。GPUメモリ設定とCloudWatch指標によるサイズ調整も扱う。

## 設計のポイント

- JumpStartの事前構築コンテナを使い、カスタム推論ハンドラなしでデプロイする。
- talkerとcode2wavの2段構成に合わせてGPUメモリを設定する。
- 文字単位のAPI課金でなく計算量ベースの課金にし、データをAWS内に留める。

## 使いどころ

- コンテンツのローカライズで話者の声を保ちたいメディアチーム。
- 自社管理の音声合成でコストとデータ統制を両立したい場面。
