---
type: case
title: 船舶ごとのML航海最適化基盤（Airflow+ECS on EC2）
title_original: 'Vessel-specific voyage optimization with machine learning: Manta on AWS'
company: Manta Marine Technologies
industry: logistics
cloud:
- aws
patterns:
- cost-optimization
- event-driven
components:
- Apache Airflow
- Amazon ECS
- Amazon EC2
- AWS Lambda
- Amazon RDS
- Amazon DynamoDB
- Amazon ECR
outcome:
  type: cost
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/vessel-specific-voyage-optimization-with-machine-learning-manta-on-aws/
published_at: '2026-10-27'
---

## 概要

Mantaは船ごとの運航履歴で個別のMLモデルを学習し、気象・海象予報と組み合わせて燃料消費を減らす。AirflowがECSタスクを使い、ETL・学習・航路最適化をEC2上で回し、新しい航海データごとに再学習する。

## 設計のポイント

- Fargateでなく命令タイプ別にキャパシティプロバイダーとASGを分け、GPUやチップ世代を制御し、Spotとオンデマンドを使い分ける。
- LambdaをAPIの入口にして、Airflow DAGの起動か処理済み結果の返却を切り替える。
- 航海完了ごとに再学習ループを回し、船固有のモデルを継続更新する。

## 使いどころ

- 個体差が大きい設備ごとにモデルを持つ予測システム。
- 大量データの学習ジョブをコスト別に実行環境へ割り振りたい場合。
