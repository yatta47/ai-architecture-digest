---
type: guidance
title: 複数アカウント・複数リージョンのSageMakerパイプラインを1画面で監視
title_original: Monitor Amazon SageMaker Pipelines cross-account with custom Amazon CloudWatch dashboards
industry: cross-industry
cloud:
- aws
patterns:
- event-driven
- llmops
components:
- Amazon SageMaker Pipelines
- Amazon CloudWatch
- Amazon EventBridge
- AWS Lambda
- Amazon DynamoDB
- Amazon SNS
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/monitor-amazon-sagemaker-pipelines-cross-account-with-custom-amazon-cloudwatch-dashboards/
published_at: '2026-07-15'
---

## 概要

複数のAWSアカウント・リージョンに分散したSageMakerパイプラインの実行状況を、アカウントを切り替えずに1つのCloudWatchダッシュボードから確認できるハブアンドスポーク型のサーバーレス監視基盤を紹介する。EventBridgeでパイプラインイベントをリアルタイムに収集・転送し、DynamoDBに集約したうえでLambda駆動のカスタムウィジェットとして可視化する。

## 設計のポイント

- 常時稼働のポーリングではなく、SageMaker Pipelineのステップ状態変化をトリガーにしたイベント駆動アーキテクチャを採用し、運用コストを抑える。
- 監視対象アカウント側は軽量なForwarderスタックのみを配置し、ダッシュボードや保存先は監視ハブ側に集約するハブアンドスポーク構成にする。
- ウィジェット呼び出し回数のしきい値超過をCloudWatchアラームで検知し、SNS経由で異常なダッシュボード利用を通知する。

## 使いどころ

- MLOpsパイプラインを複数のAWSアカウント・リージョンにまたがって運用しているチーム。
- アカウント切り替えの手間を減らし、単一画面でパイプライン実行状況を俯瞰したい運用担当者。
- サーバーレスかつイベント駆動で監視基盤を構築し、常時起動のポーリング基盤を避けたい場合。
