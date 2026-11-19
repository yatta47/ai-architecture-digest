---
type: announcement
title: SageMaker AIサーバーレスのモデルカスタマイズが全パラメータ微調整に対応
title_original: Full Fine-Tuning (FFT) on SageMaker AI Serverless Model Customization
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- fine-tuning
components:
- Amazon SageMaker AI
- SageMaker AI Serverless Model Customization
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/full-fine-tuning-fft-on-sagemaker-ai-serverless-model-customization/
published_at: '2026-11-19'
---

## 概要

SageMaker AIのサーバーレスモデルカスタマイズがFull Fine-Tuningに対応した。LoRAの低ランク制約による表現力の限界を超え、複雑なタスクで高い品質を得られ、GPU確保やクラスタ構築は不要。ベンチマークとハイパーパラメータ指針も示される。

## 設計のポイント

- 複雑なドメイン知識の取り込みでは、LoRAでなくFFTを選ぶ判断基準を持つ。
- インフラ管理をサーバーレスに任せ、微調整の設計に集中できる。
- 小型の特化モデルで大型モデルに並ぶ精度を狙い、推論単価を下げる。

## 使いどころ

- ドメイン特化モデルでLoRAの精度が頭打ちになったチーム。
- GPUクラスタを持たずに微調整したい組織。
