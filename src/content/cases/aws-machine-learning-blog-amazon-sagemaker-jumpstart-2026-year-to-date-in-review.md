---
type: guidance
title: SageMaker JumpStartの2026年1〜9月の動向まとめ
title_original: 'Amazon SageMaker JumpStart: 2026 year-to-date in review'
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- fine-tuning
- inference-optimization
- llmops
components:
- Amazon SageMaker JumpStart
- Amazon SageMaker Studio
- Hugging Face
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-jumpstart-2026-year-to-date-in-review/
published_at: '2026-10-19'
---

## 概要

SageMaker JumpStartは2026年1〜9月に30プロバイダーから100超のモデルを追加した。モデルの探索・評価、設定済みエンドポイントへのワンクリックデプロイ、LoRA・SFT・DPO・RLVRによるカスタマイズを一つのハブで提供する。

## 設計のポイント

- デプロイ設定をコスト・遅延・スループット・バランスの目的別プリセットで提供し、コンテナやインスタンスの手動設定を省く。
- サーバーレスのカスタマイズでファインチューニングのインフラ管理を減らす。
- Hugging Faceからのディープリンクでモデル選定から展開までの動線を短縮する。

## 使いどころ

- オープンLLMを比較・評価して自社で展開したいチーム。
- 小型モデルを自社データでファインチューニングしたい場面。
