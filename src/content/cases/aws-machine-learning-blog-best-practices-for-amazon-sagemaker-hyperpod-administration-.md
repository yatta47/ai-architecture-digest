---
type: guidance
title: SageMaker HyperPod共有クラスタの4層ガバナンス設計
title_original: Best practices for Amazon SageMaker HyperPod administration and governance
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- gpu-fleet-reliability
- policy-as-code
- cost-optimization
components:
- Amazon SageMaker HyperPod
- Amazon SageMaker Unified Studio
- Amazon EKS
- AWS IAM
- AWS KMS
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/best-practices-for-amazon-sagemaker-hyperpod-administration-and-governance/
published_at: '2026-10-06'
---

## 概要

複数チームでSageMaker HyperPodクラスタを共有する際のガバナンスを、組織・プロジェクト・クラスタ・ワークロードの4層で整理したガイド。Unified Studioのプロジェクト接続を使いつつ、クラスタ側のIAM/EKS/Slurm制御を維持する運用モデルを示す。

## 設計のポイント

- プロジェクト接続はクラスタ側のIAM・RBACを置き換えないため、各層の制御を揃えてから公開する。
- 計算割り当て・優先度クラス・貸借ポリシーで共有GPU容量の競合を制御する。
- クラスタ運用はインフラチーム、利用は各MLチームという責務分離を保つ。

## 使いどころ

- 複数のMLチームで共有GPUクラスタを運用する基盤チーム。
- 社内ML基盤をセルフサービス化しつつ統制したい場面。
