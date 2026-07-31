---
type: guidance
title: SageMakerエンドポイントのメタ監視基盤をQuickとMLflowで構築する
title_original: Inference meta-monitoring for Amazon SageMaker AI endpoints with Amazon Quick
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- eval
components:
- Amazon SageMaker AI
- Amazon Athena
- AWS Lambda
- Amazon EventBridge
- Amazon Quick
- SageMaker AI MLflow
- Evidently AI
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/inference-meta-monitoring-for-amazon-sagemaker-ai-endpoints-with-amazon-quick/
published_at: '2026-07-30'
---

## 概要

本番MLエンドポイントの予測品質やデータドリフトを継続監視する「推論メタ監視」の構築手順を解説する記事。学習・推論・監視の各パイプラインをAthena Icebergテーブルを中核に統合し、SQS経由でLambdaがログを書き込み、Amazon QuickとMLflowでドリフトの可視化と遅延グラウンドトゥルースの取り込みを行う。

## 設計のポイント

- 学習時のholdoutデータをドリフト監視の固定ベースラインとし、決定的ハッシュ分割で再実行しても同じ分割を保つ
- 推論ログはSQS→Lambdaでバッチ化し、Athena Icebergテーブルへ非同期に書き込んでレイテンシ影響を避ける
- グラウンドトゥルースが遅延して届く業務（不正検知など）を前提に、後追いラベル付けの取り込み経路を別途用意する
- MLflowでの実験管理とQuickダッシュボードを同一データレイクの上に重ねてガバナンス層として提供する

## 使いどころ

- 不正検知・与信スコアリング・需要予測など予測精度の劣化に気づきにくいモデルを運用するチーム
- 顧客からのクレームで初めて精度劣化に気づく状態を脱したいMLOps担当者
- 遅延グラウンドトゥルースを伴う業務でモデル性能の継続的な可視化を必要とする組織
