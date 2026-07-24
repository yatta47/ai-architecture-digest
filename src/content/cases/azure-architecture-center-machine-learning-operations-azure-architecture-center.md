---
type: guidance
title: MLOps v2による機械学習運用アーキテクチャ
title_original: Machine learning operations
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- mlops
- ci-cd
components:
- Azure Machine Learning
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/machine-learning-operations-v2
published_at: '2024-07-12'
---

## 概要

古典的機械学習、コンピュータビジョン、自然言語処理の3領域について、CI/CDと再学習パイプラインを備えたエンドツーエンドのMLOpsアーキテクチャをAzure Machine Learningで実現する方法を解説する。MLOps v2プロジェクトの知見から導かれた、再現可能で保守しやすいパターンを提示する。

## 設計のポイント

- データ基盤・管理設定・モデル開発(インナーループ)・モデル運用の4フェーズでMLOpsライフサイクルをモジュール化する
- 分類/CV/NLPというユースケース別にリファレンスアーキテクチャとデプロイテンプレートを用意し再利用可能にする

## 使いどころ

- 表形式データの時系列予測や分類など古典的MLモデルを継続的に再学習・デプロイしたいチーム
- 画像セグメンテーションやテキスト分類などCV/NLPモデルを本番運用するプロジェクト
