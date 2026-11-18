---
type: announcement
title: SageMakerにAIデータ準備機能（合成データ生成・ラベリング・品質評価）
title_original: Announcing AI data preparation capabilities in Amazon SageMaker
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- fine-tuning
- eval
components:
- Amazon SageMaker AI
- Python SDK
- AWS AI-ML agent skill
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/announcing-ai-data-preparation-capabilities-in-amazon-sagemaker-build-high-quality-datasets-for-model-development-workflows/
published_at: '2026-11-17'
---

## 概要

SageMaker AIがファインチューニングや強化学習、評価セット作成のためのデータ準備機能を追加した。自動ラベリング、合成サンプル生成、既存データの評価・改善、専門家フィードバックの取り込みをPython SDKとエージェントスキルから単体または連結で使える。

## 設計のポイント

- 各機能を独立したビルディングブロックとして連結可能にする。
- 重複・ラベルノイズ・リークなどの品質問題を学習前に検出する。
- ノートブックやIDE上で検査・変更できる仕様とコードで進める。

## 使いどころ

- 小型モデルをタスク特化データでカスタマイズしたいチーム。
- 評価データの作成コストを下げたいML担当。
