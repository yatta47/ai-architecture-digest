---
type: guidance
title: SageMaker HyperPodでGPUクラスタを複数チームで安全に共有するマルチテナント構成
title_original: Share GPU clusters across teams with isolation and fairness using Amazon SageMaker HyperPod
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- gpu-fleet-reliability
- policy-as-code
- cost-optimization
components:
- Amazon SageMaker HyperPod
- Amazon EKS
- AWS IAM Identity Center
- HyperPod Task Governance
- Amazon FSx for Lustre
- Amazon S3
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/share-gpu-clusters-across-teams-with-isolation-and-fairness-using-amazon-sagemaker-hyperpod/
published_at: '2026-10-08'
---

## 概要

1つのHyperPod EKSクラスタを複数チームで共有するためのリファレンスアーキテクチャ。IAM Identity Centerによる認証、チーム別SageMakerドメイン、Kubernetes名前空間による分離、Task Governanceによる公平なリソース配分、名前空間単位のコスト配賦を組み合わせる。

## 設計のポイント

- 認証から認可、ワークロード実行までをチーム単位の名前空間とIAMロールで一貫して分離する。
- Task Governanceで計算クォータと優先度を管理し、高価なGPUの奪い合いを防ぐ。
- 名前空間単位のコスト配賦でチーム別の課金・チャージバックを可能にする。

## 使いどころ

- 複数のデータサイエンス・研究チームで高価なGPUクラスタを共有したい組織に効く。
- GPUコストをチームへ按分したい基盤チームの設計の出発点になる。
