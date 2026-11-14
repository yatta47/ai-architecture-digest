---
type: guidance
title: HyperPod Data Captureで本番推論を記録し、再学習へつなぐ改善ループ
title_original: Build a model improvement flywheel with Amazon SageMaker HyperPod Data Capture
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- fine-tuning
- eval
components:
- Amazon SageMaker HyperPod
- Amazon S3
- Amazon Athena
- Application Load Balancer
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-model-improvement-flywheel-with-amazon-sagemaker-hyperpod-data-capture/
published_at: '2026-11-13'
---

## 概要

HyperPodの新機能Data Captureは、本番推論の入出力をS3へ3階層で記録する。家電サポートのルーターを例に、Athenaで新製品の死角を見つけ、SQLポリシーでラベル付けし、ファインチューニングで精度が改善することを示す。

## 設計のポイント

- エンドポイント、ロードバランサ、モデルPodの3層を独立に選んでキャプチャする。
- 記録データをAthenaで分析しドリフトや失敗パターンを検出する。
- キャプチャ→ラベル付け→ファインチューニング→前後比較を一つのクラスタ内で回す。

## 使いどころ

- 本番トラフィックでモデルを継続改善したい基盤チーム。
- ドリフトや新規ドメイン語への対応が必要な分類・ルーティングモデルの運用者。
