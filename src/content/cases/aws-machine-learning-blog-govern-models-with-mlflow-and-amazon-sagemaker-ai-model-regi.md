---
type: guidance
title: MLflow×SageMakerモデルレジストリ同期によるクロスアカウントモデルガバナンス
title_original: 'Govern models with MLflow and Amazon SageMaker AI Model Registry sync: Part 2'
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- human-in-the-loop
components:
- Amazon SageMaker AI
- MLflow
- AWS RAM
- AWS IAM
- Amazon S3
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/govern-models-with-mlflow-and-amazon-sagemaker-ai-model-registry-sync-part-2/
published_at: '2026-09-08'
---

## 概要

開発アカウントと本番/ガバナンスアカウントを分離する大規模組織向けに、Amazon SageMaker AI上のマネージドMLflowとモデルレジストリをクロスアカウントで同期する2つのトポロジーを解説する。AWS RAMによるハブアンドスポーク型の集中ガバナンスと、規制環境向けに開発アカウントを完全分離するハイブリッド型を比較し、承認済みモデルがCI/CDでエンドポイントへ展開されるまでの流れを示す。

## 設計のポイント

- AWS RAMでMLflowアプリとモデルパッケージグループをクロスアカウント共有し、外部プリンシパルにも対応する
- IAM条件キーでデータサイエンティストとガバナンス担当者のペルソナ別アクセスを分離する
- モデル中央承認イベントをトリガーにCI/CDパイプラインでスポークアカウントへデプロイする

## 使いどころ

- 複数の開発アカウントと中央ガバナンス機能を持つ大規模組織のモデル管理
- 規制業界で開発ワークロードが本番グレードアカウントに書き込めない要件がある場合
