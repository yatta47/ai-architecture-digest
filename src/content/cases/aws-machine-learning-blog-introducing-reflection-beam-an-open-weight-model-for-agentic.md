---
type: guidance
title: オープンウェイトのコーディングモデルBeamをAWSで配信する手引き
title_original: 'Introducing Reflection Beam: an open-weight model for agentic coding on AWS'
company: Reflection AI
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- ai-agent
components:
- Amazon SageMaker JumpStart
- Amazon SageMaker HyperPod Inference
- Amazon EKS
- SGLang
- vLLM
- Hugging Face
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-reflection-beam-an-open-weight-model-for-agentic-coding-on-aws/
published_at: '2026-10-16'
---

## 概要

Reflection AIの総パラメータ501B・アクティブ23BのMoEモデルBeamを、SageMaker JumpStartのリアルタイムエンドポイントとHyperPod Inferenceの2経路でAWSに配備する手順を解説する。チェックポイント形式（BF16/FP8/NVFP4）ごとにGPUインスタンスと並列化の考え方が変わる。

## 設計のポイント

- マネージド重視のJumpStartエンドポイントと、Kubernetesで実行系を制御できるHyperPod Inferenceを要件で使い分ける。
- BF16・FP8・NVFP4の量子化形式で必要なGPUメモリとインスタンスが決まるため、重み・KVキャッシュ・オーバーヘッドから容量を見積もり負荷試験で確認する。
- 同時実行数とレイテンシ目標を先に決め、レプリカ・キャッシュ・ルーティング・オートスケールは実測で調整する。

## 使いどころ

- 自社AWSアカウント内でオープンウェイトのコーディングエージェント用モデルを運用したい基盤チーム。
- 大規模MoEモデルのGPU容量計画とサービング方式を検討する場面。
