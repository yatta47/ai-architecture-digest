---
type: announcement
title: SageMaker JumpStartでNemotron 3.5 Super VLが利用可能に
title_original: NVIDIA Nemotron 3.5 Super VL is now available in Amazon SageMaker JumpStart
company: NVIDIA / AWS
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
components:
- NVIDIA Nemotron 3.5 Super VL
- Amazon SageMaker JumpStart
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/nvidia-nemotron-3-5-super-vl-is-now-available-in-amazon-sagemaker-jumpstart/
published_at: '2026-11-09'
---

## 概要

120B(アクティブ12B)のMoE視覚言語モデルがSageMaker JumpStartから展開できる。NVFP4とBF16の2種類があり、100万トークン文脈や投機的デコードに対応する。文書理解やコンピュータ操作エージェント向けである。

## 設計のポイント

- 量子化版と全精度版を選べる。
- リクエスト単位で推論設定を切り替える。

## 使いどころ

- 文書理解や動画QAのマルチモーダル基盤
