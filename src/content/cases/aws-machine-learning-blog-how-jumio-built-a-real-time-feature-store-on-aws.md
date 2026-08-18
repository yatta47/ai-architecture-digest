---
type: case
title: Jumioが構築したAWS上のリアルタイム特徴量ストア
title_original: How Jumio built a real-time feature store on AWS
company: Jumio
industry: financial-services
cloud:
- aws
patterns:
- feature-store
- event-driven
- inference-optimization
components:
- Amazon SageMaker Feature Store
- Amazon Managed Service for Apache Flink
- Amazon Kinesis Data Streams
- Amazon Data Firehose
- Amazon S3
- Amazon EMR
- Amazon EMR Serverless
- Apache Iceberg
- Amazon ElastiCache for Valkey
- Amazon Athena
- AWS Lambda
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-jumio-built-a-real-time-feature-store-on-aws/
published_at: '2026-08-18'
---

## 概要

本人確認・不正検知を手がけるJumioは、特徴量の重複管理やオフライン学習と本番実装のロジック不一致、100ミリ秒未満のレイテンシ要件に対応するため、Kinesis・Flink・SageMaker Feature Storeを核としたリアルタイム特徴量ストアを3リージョンに構築した。リアルタイム経路とS3・EMR・Icebergによるオフライン経路を並走させ、モデル推論と再学習の両方を単一の特徴量基盤から支える。

## 設計のポイント

- Kinesis Data StreamsとFlinkでイベントをリアルタイムに特徴量へ変換しSageMaker Feature Storeへ直接書き込むホットパスと、Firehose経由でS3・EMRからIcebergテーブルへ流すオフラインパスを並列運用する
- SageMaker Feature Store内でElastiCache for Valkeyによるホットデータ(低レイテンシ読み書き)と標準ストアのコールドデータ(スケーラブルで安価)を使い分け、コストとレイテンシのバランスを取る
- Kinesis→Flink→Sink→Feature Storeまでの各段階でレイテンシを個別に監視し、不正検知に必要な100ミリ秒未満のSLAを段階ごとに担保する
- オフライン側はS3イベント通知でLambda経由のEMR Serverlessを起動しIcebergテーブルを更新することで、モデル再学習・デバッグ・監視用データを近リアルタイムで用意する

## 使いどころ

- 不正検知など100ミリ秒未満でモデル推論用の特徴量を提供する必要があるリアルタイムML基盤
- オフライン学習時の特徴量定義と本番推論時の実装がズレて不整合が生じている組織の特徴量統合
- 複数チームが独立して特徴量を追加・変更できる、疎結合な特徴量開発体制を目指す場合
