---
type: case
title: カメラごとの欠陥検出モデルを回すSageMakerエッジMLOps
title_original: Fleet-wide computer vision lifecycle at the edge with SageMaker SDK v3
company: AWS
industry: manufacturing
cloud:
- aws
patterns:
- llmops
- parallel-execution
- event-driven
components:
- Amazon SageMaker Pipelines
- SageMaker Neo
- SageMaker Model Registry
- AWS Step Functions
- Amazon SQS
- Amazon DynamoDB
- AWS CDK
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/
published_at: '2026-10-26'
---

## 概要

工場の多数のカメラごとに異常検知器と欠陥分類器を学習するSageMaker Pipelineを、SDK v3で再構成した。品質ゲートで劣化モデルを止め、Neoでデバイス向けにコンパイルし、SQSとStep Functionsで再学習の同時実行を制限する。

## 設計のポイント

- カメラIDをメタデータに付け、再学習をそのカメラの履歴から再開する。
- 品質ゲート通過後にだけNeoコンパイルとモデル登録を行う。
- DynamoDBセマフォで並列度を制限し、アカウント上限内に収める。

## 使いどころ

- 多数の拠点・カメラで個別モデルを運用する製造業。
- 大量モデルの再学習を自動化したい場合。
