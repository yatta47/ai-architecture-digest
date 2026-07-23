---
type: announcement
title: Kubernetesにチェックポイント/リストアを統合するWG発足
title_original: Announcing the Checkpoint/Restore Working Group
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- disaster-recovery
- gpu-fleet-reliability
components:
- CRIU
- checkpointctl
- criu-coordinator
- checkpoint-restore-operator
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/01/21/introducing-checkpoint-restore-wg/
published_at: '2026-01-21'
---

## 概要

KubernetesコミュニティがCheckpoint/Restore Working Groupの発足を発表。JupyterノートブックやAIチャットボットなど対話型ワークロードのリソース最適化、LLM推論サービスなど起動が重いアプリの高速化、分散モデル学習の耐障害性確保のための定期チェックポイント、中断を意識したスケジューリングやPod移行、フォレンジック用途まで、CRIUエコシステムとKubernetesを統合するユースケースを議論する場として設立された。

## 設計のポイント

- CRIUベースのプロセスチェックポイント/リストアをKubernetesに統合し、Podの実行状態を保存・復元可能にする
- 定期的なチェックポイントを取ることで、長時間実行される分散学習ジョブに耐障害性を持たせる
- criu-coordinatorにより分散アプリケーション全体を協調させてチェックポイント/リストアする
- プリエンプション時にランタイム状態を保持したまま低優先度Podを退避させる中断考慮スケジューリングを実現する

## 使いどころ

- Jupyterノートブックやチャットボットなど対話型ワークロードのリソース利用を最適化したい場合
- 起動に時間のかかるLLM推論サービスやJavaアプリケーションの立ち上げを高速化したい場合
- ノード間でPodを移行してもワークロードを中断させずにメンテナンスや負荷分散を行いたい場合
- セキュリティインシデント調査のためにコンテナの実行状態をフォレンジック的に保存したい場合
