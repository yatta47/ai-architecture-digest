---
type: guidance
title: MLOpsで実現する機械学習パイプラインの継続的デリバリーと自動化
title_original: 'MLOps: Continuous delivery and automation pipelines in machine learning'
industry: cross-industry
cloud:
- gcp
patterns:
- mlops
- ci-cd
components: []
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
published_at: '2026-07-19'
---

## 概要

MLシステムにDevOpsの原則を適用するMLOpsの考え方を整理したガイド。コード・データ・モデルという3つの対象を継続的に検証・統合・デプロイする点が通常のソフトウェア開発と異なると説明する。データサイエンティストとエンジニアリングチームのスキル差やモデル劣化への対応など、ML特有の課題にも触れている。

## 設計のポイント

- CIはコードだけでなくデータスキーマやモデル品質の検証も対象に含める
- CDは単一パッケージではなく、再学習・再デプロイまで含むMLパイプライン全体を対象にする
- CT(継続的トレーニング)というML特有の概念を導入し、データドリフトに応じて自動再学習・再配信する
- モデルの性能劣化を検知するため本番のデータ分布とモデル出力を継続的に監視する

## 使いどころ

- データサイエンスチームとソフトウェアエンジニアリングチームが分業している組織でML運用を標準化したい場合
- 本番投入後にデータ分布の変化でモデル精度が劣化する課題を抱えるチーム
