---
type: guidance
title: SageMaker JumpStartでモデルをデプロイし性能を再現的に測る手順
title_original: Deploy and evaluate models with Amazon SageMaker JumpStart
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- eval
- inference-optimization
components:
- Amazon SageMaker JumpStart
- SageMaker Python SDK
- SageMaker Studio
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/deploy-and-evaluate-models-with-amazon-sagemaker-jumpstart/
published_at: '2026-10-14'
---

## 概要

JumpStartのモデルを探索・デプロイし、代表プロンプトでレイテンシや生成速度を測定してエンドポイントを削除する再利用可能なPythonスクリプトの手引き。低コスト・低レイテンシ等の構成プリセットやHugging Faceからのワンクリックデプロイも紹介する。

## 設計のポイント

- 発見→デプロイ→計測→削除を一連のスクリプトにして、モデル選定を再現可能にする
- 低コスト/低レイテンシなど優先度別のプリセット構成を使う
- GPUクォータやEULAなどモデル固有の前提を事前確認する

## 使いどころ

- アプリに合うモデルを本番前に比較したい開発者
- 評価用エンドポイントの消し忘れによるコストを避けたいチーム
