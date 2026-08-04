---
type: announcement
title: Kubeflow SDK、分散学習からチューニングまでを単一のPython APIに統合
title_original: 'Kubeflow SDK Evolution: One Million Downloads and Counting'
industry: cross-industry
cloud: []
patterns:
- unified-runtime
- llmops
- fine-tuning
components:
- kubeflow-sdk
- TrainerClient
- OptimizerClient
- SparkClient
- PipelinesClient
- Kubeflow Trainer
- Katib
- Model Registry
- Kubernetes
- TrainJob CRD
- PyTorch
- DeepSpeed
- TensorFlow
- Model Context Protocol
outcome:
  type: productivity
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/03/kubeflow-sdk-evolution-one-million-downloads-and-counting/
published_at: '2026-08-03'
---

## 概要

Kubeflowコミュニティは、kubeflow-training・katib・model-registryなど乱立していた個別SDKを1つのimport kubeflowに統合し、TrainerClientとOptimizerClientを皮切りに2025年11月にpip install kubeflowとして公開した。PythonのみでYAML記述やkubectl操作なしに分散学習・ハイパーパラメータ調整・パイプライン管理まで行えるこのSDKは、公開から1年足らずでPyPIダウンロード数100万件を突破した。

## 設計のポイント

- 複数のサブプロジェクト専用SDKを廃し、単一のPython importの下にTrainerClient/OptimizerClient/SparkClient/PipelinesClientなど機能別クライアントを集約する設計にした。
- ローカルプロセス・コンテナ(Docker/Podman)・Kubernetesの3つの実行バックエンドを同一APIで提供し、設定変更1行だけでラップトップから本番クラスタへ移行できるようにした。
- AI実践者(データサイエンティスト/MLエンジニア)とプラットフォーム管理者の役割を明確に分離し、実践者側はYAMLやkubectlに一切触れずPythonのみで完結できるようにした。
- トレーニング関数をシリアライズしてTrainJob CRDを動的生成・投入し、MASTER_ADDR/WORLD_SIZE/RANKなど分散実行に必要な環境変数の設定を自動化した。

## 使いどころ

- Kubernetesや分散システムの専門知識を持たないML/データサイエンティストが、YAMLを書かずに分散学習ジョブを投入したい場面。
- ローカルでの高速なプロトタイピングから本番Kubernetesクラスタでのスケール実行まで、コードを書き換えずに段階的に移行したいチーム。
- ハイパーパラメータチューニング(Katib)、モデルレジストリ、Sparkによる大規模データ前処理、パイプライン管理を一貫したPython APIでまとめて扱いたい場合。
