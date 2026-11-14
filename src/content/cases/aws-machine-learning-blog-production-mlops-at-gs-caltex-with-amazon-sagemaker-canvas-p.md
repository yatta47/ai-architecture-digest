---
type: case
title: GS CaltexがSageMaker CanvasのモデルをPipelinesで本番バッチ推論に載せるMLOps
title_original: Production MLOps at GS Caltex with Amazon SageMaker Canvas, part 1
company: GS Caltex
industry: manufacturing
cloud:
- aws
patterns:
- llmops
- cost-optimization
components:
- Amazon SageMaker Canvas
- Amazon SageMaker Pipelines
- Amazon SageMaker Model Registry
- Amazon SageMaker Processing
- Data Wrangler
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/production-mlops-at-gs-caltex-with-amazon-sagemaker-canvas-part-1/
published_at: '2026-11-13'
---

## 概要

GS Caltexは、プロセスエンジニアがノーコードで作ったSageMaker Canvasのモデルを、MLエンジニアがSageMaker Pipelinesで本番化する分業体制を構築した。Canvas資産からPipelinesへの引き継ぎを自動化し、デプロイが約1週間から数時間に短縮、30分ごとのバッチ推論で推論コストも削減した。

## 設計のポイント

- ドメイン知識を持つ人（Canvas）と運用担当（Pipelines）で役割を分け、Model Registryの承認状態を接点にする。
- Canvasで作った前処理フローとモデルを再利用し、パイプライン化の手作業を自動化する。
- 常時エンドポイントでなく30分ごとのバッチ推論にしてコストを抑える。

## 使いどころ

- 現場エンジニア主導のモデル開発を、運用品質を保ったまま本番化したい製造・エネルギー企業。
- ノーコードMLと本番MLOpsの橋渡しに悩む組織。
