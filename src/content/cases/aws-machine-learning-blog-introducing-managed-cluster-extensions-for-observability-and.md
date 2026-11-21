---
type: announcement
title: SageMaker HyperPod Slurmの宣言的クラスタ管理とクラスタ拡張
title_original: Introducing managed cluster extensions for observability and user management in Amazon SageMaker HyperPod
  Slurm
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- gpu-fleet-reliability
- policy-as-code
components:
- Amazon SageMaker HyperPod
- Slurm
- Amazon FSx for Lustre
- Amazon FSx for OpenZFS
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-managed-cluster-extensions-for-observability-and-user-management-in-amazon-sagemaker-hyperpod-slurm/
published_at: '2026-11-20'
---

## 概要

基盤モデル開発用の共有Slurmクラスタで、設定のずれを防ぐためにAPIによる宣言的管理をノード上のソフトウェアにまで広げるクラスタ拡張を発表した。観測性とユーザー管理のマネージド拡張が対象で、全ノードへの直接アクセスも残している。

## 設計のポイント

- クラスタ設定を6層に分け、宣言し、検証し、継続的に維持する方式を各層に広げる。
- API管理と直接SSHの両方を残し、運用者が自動化と制御のバランスを選べる。
- ノード交換時もトポロジーなどを自動維持する。

## 使いどころ

- 大規模学習用Slurmクラスタの設定ドリフトを減らしたいとき。
- ユーザー管理や監視の構築をプラットフォームチームの手作業から外したいとき。
