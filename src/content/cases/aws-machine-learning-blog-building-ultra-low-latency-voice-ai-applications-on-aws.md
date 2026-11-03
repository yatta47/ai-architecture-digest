---
type: case
title: Cartesia：SSMで100ms未満の音声合成・認識をAWS上に提供
title_original: Building ultra-low-latency voice AI applications on AWS
company: Cartesia
industry: cross-industry
cloud:
- aws
patterns:
- voice-agent
- inference-optimization
components:
- Cartesia
- State Space Models
- AWS
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-ultra-low-latency-voice-ai-applications-on-aws/
published_at: '2026-11-03'
---

## 概要

AWSパートナーのCartesiaが、状態空間モデル（SSM）とAWSインフラで100ms未満のTTS/STTをグローバル規模で実現する方法を紹介する。トランスフォーマーはストリーミング遅延に弱く、SSMは固定状態を持ち越して逐次処理できる点が音声に適する。

## 設計のポイント

- 注意機構の二乗計算を避けるSSMでストリーミング音声の遅延と品質のトレードオフを緩和する
- 人間の会話のターンテイキングに収まる応答時間を設計目標とする
- コンタクトセンターやゲームなど用途横断で同一の低遅延基盤を使う

## 使いどころ

- AIコンタクトセンターや音声営業エージェント
- 遠隔診療・NPC・アクセシビリティなど即応性が必要な音声UI
