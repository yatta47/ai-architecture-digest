---
type: announcement
title: KubeflowのML資源をKubernetes UIに直接表示するHeadlampプラグイン
title_original: 'Operating AI/ML Workloads on Kubernetes: A Headlamp Plugin for Kubeflow'
industry: cross-industry
cloud: []
patterns:
- llmops
- root-cause-analysis
components:
- Headlamp
- Kubeflow
- Kubernetes
- Katib
- Kubeflow Pipelines
- Apache Spark
- PyTorch
- TensorFlow
- Jupyter
data_sources:
- Kubernetes APIリソース
- CRD
- Podステータス
outcome:
  type: productivity
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/07/13/introducing-headlamp-plugin-for-kubeflow/
published_at: '2026-07-13'
---

## 概要

Kubernetesは今やAI/MLワークロードの標準基盤となり、Kubeflowはノートブック・分散学習・ハイパーパラメータ調整・パイプラインなどの機能をすべてCRDとして公開する。しかし専用MLダッシュボードはKubernetes層を隠すため、運用者はnotebookのstuckや学習失敗の原因をPodレベルで探る際にkubectlへ戻らざるを得なかった。本記事は、KubeflowのカスタムリソースをHeadlamp（Apache 2.0の汎用Kubernetes Web UI）内に直接表示し、そのギャップを埋めるプラグインを紹介する。

## 設計のポイント

- Kubernetes APIサーバから直接リソースを読み取り、Kubeflow Pipelinesのバックエンドや中間MLサービスに依存させない。それらの停止中でも保存済みの状態を確認できる
- インストール済みのAPIグループ（Notebooks/Pipelines/Katib/Training/Spark）を自動検出し、該当セクションだけを表示するモジュラー設計にする
- ownerReferencesを辿ってリソース間の関係をグラフ表示する
- CRD中心のあらゆるプラットフォームに応用できる『運用者が既に使う場所でクラスタの真実を見せる』パターンとして提示する

## 使いどころ

- notebookでImagePullBackOffやOOMKilled、学習ジョブの失敗をPodの条件・理由からその場で調べたいクラスタ運用者やSRE
- 専用MLダッシュボードとkubectlを行き来せず、単一のKubernetes UIで名前空間横断の状態把握を完結させたい場面
- トラブルシュートを別ツールに切り替えず1つのUIで済ませたい運用現場
