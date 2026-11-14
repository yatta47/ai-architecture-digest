---
type: guidance
title: OpenFold3をSageMaker JumpStartの非同期エンドポイントで生体分子構造予測に使う
title_original: 'OpenFold3 on Amazon SageMaker JumpStart: Predict biomolecular structures'
company: AWS
industry: healthcare
cloud:
- aws
patterns:
- inference-optimization
- cost-optimization
components:
- Amazon SageMaker JumpStart
- SageMaker asynchronous inference
- OpenFold3
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/openfold3-on-amazon-sagemaker-jumpstart-predict-biomolecular-structures/
published_at: '2026-11-13'
---

## 概要

オープンソースの構造予測モデルOpenFold3を、JumpStartから非同期推論エンドポイントとして自アカウントにデプロイする手順。ネットワーク分離、マルチGPUでの並列予測、独自MSAの持ち込み、アイドル時のゼロスケールによるコスト削減を扱う。

## 設計のポイント

- 数分かかる推論を非同期エンドポイントとキューイングで処理する。
- ネットワーク分離と独自MSAの持ち込みで配列データを自アカウント内に留める。
- アイドル時にゼロへスケールしてGPUコストを抑える。

## 使いどころ

- 創薬での構造予測基盤を自社AWSで持ちたいチーム。
- GPU基盤を自前構築せずに大規模モデルを配信したい研究組織。
