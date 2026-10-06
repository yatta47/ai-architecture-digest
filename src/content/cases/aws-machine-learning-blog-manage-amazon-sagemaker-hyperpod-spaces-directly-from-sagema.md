---
type: announcement
title: SageMaker StudioからHyperPod Spacesを操作できる機能
title_original: Manage Amazon SageMaker HyperPod Spaces directly from SageMaker Studio
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- gpu-fleet-reliability
- cost-optimization
components:
- Amazon SageMaker HyperPod
- Amazon SageMaker Studio
- Amazon EKS
- JupyterLab
- Code Editor
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/manage-amazon-sagemaker-hyperpod-spaces-directly-from-sagemaker-studio/
published_at: '2026-10-06'
---

## 概要

HyperPod EKSクラスタ上のJupyterLab/Code Editor環境（Spaces）を、SageMaker StudioのUIから作成・起動・停止できるようになった。従来のCLI/kubectl中心の運用を、データサイエンティスト向けのGUIで置き換える。

## 設計のポイント

- 管理者が一度アドオンとEKSアクセスエントリを設定し、利用者はGUIだけで環境を扱う分業にする。
- タスクガバナンスと部分GPU割り当てで、対話環境を学習・推論と同じ基盤に同居させる。
- 未使用Spaceの停止を簡単にして計算資源を解放する。

## 使いどころ

- GPUクラスタをCLIなしで使わせたいデータサイエンティスト向け基盤。
- 学習と開発環境でGPU投資を使い切りたい組織。
