---
type: announcement
title: SageMaker HyperPod上でRayクラスタをKubernetes知識なしで運用できるように
title_original: Introducing New Ray Capabilities on SageMaker HyperPod
industry: cross-industry
cloud:
- aws
patterns:
- gpu-fleet-reliability
- inference-optimization
- unified-runtime
- llmops
components:
- Amazon SageMaker HyperPod
- Ray
- KubeRay
- Amazon EKS
- Amazon Managed Grafana
- Amazon SageMaker JumpStart
- SageMaker Studio
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-new-ray-capabilities-on-sagemaker-hyperpod/
published_at: '2026-08-24'
---

## 概要

AWSは、基盤モデルの分散学習・配信フレームワークRayをSageMaker HyperPod上でネイティブに扱える新機能を発表した。データサイエンティストはYAMLマニフェストやkubectlポートフォワードを書かずに、SageMaker StudioからRayクラスタの作成・Ray Dashboard/Grafanaでの監視・JupyterLab/Code Editorからの接続・リモートジョブ投入までを行える。HyperPodのノードヘルス監視・自動リカバリによる学習ジョブのフォールトトレランスや、階層型ストレージを使ったチェックポイント再開・KVキャッシュオフロードも組み込まれている。

## 設計のポイント

- 既存のOSS KubeRay・標準Ray APIとの互換性を保ったまま、Kubernetesマニフェストを書かずに使えるマネージド体験をStudio上に重ねている
- 学習ジョブの耐障害性をアプリケーション層(Ray)ではなく基盤層(HyperPodのノードヘルス監視・自動リカバリ)に持たせ、階層型ストレージでチェックポイント再開を高速化する
- 推論(Ray Serve)側はSageMaker JumpStartでモデル重みを直接ロードし、長文コンテキスト配信のためにKVキャッシュを階層型ストレージへオフロードする
- IAM認証付きの短命URLでRay Dashboardやリモートジョブ投入を提供し、ローカルのkubectlポートフォワード無しで安全にアクセスできるようにする

## 使いどころ

- Kubernetesの専門知識を持たないデータサイエンティストが分散学習・配信ジョブを自分で立ち上げたい場合
- ノートブックでの少数ワーカーのプロトタイピングから、GPUクラスタでの本番学習・配信までシームレスにスケールしたいチーム
- 既存のRay/KubeRayスクリプトを変更せずに、可観測性（Grafana）と障害復旧を基盤側でまとめて手に入れたい場合
