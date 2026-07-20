---
type: announcement
title: Kubernetes上のGPU利用状況をワンコマンドで可視化するGPU Usage Monitor
title_original: Get Real-Time Visibility into GPU Usage Across Kubernetes Clusters
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- gpu-fleet-reliability
- cost-optimization
- root-cause-analysis
components:
- GPU Usage Monitor
- NVIDIA DCGM Exporter
- kube-state-metrics
- Prometheus
- Grafana
- NVIDIA GPU Operator
- Helm
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/get-real-time-visibility-into-gpu-usage-across-kubernetes-clusters/
published_at: '2026-07-09'
---

## 概要

NVIDIAはKubernetesクラスタ上のGPU利用状況を可視化するオープンソースツール「GPU Usage Monitor」を公開した。DCGM Exporter・kube-state-metrics・Prometheus・Grafanaを単一のHelmチャートに統合し、GPUの割り当て・使用率・メモリ消費・pod状態を1つのダッシュボードで把握できるようにする。モデルがGPUメモリ・計算資源の30〜50%しか使わない過剰プロビジョニングや、GPU要求がPending状態で滞留するスケジューリングブロッカーを、ユーザー報告前に検知できることを狙いとしている。

## 設計のポイント

- DCGM ExporterでGPUハードウェアメトリクスを、kube-state-metricsでKubernetesのpod/リソースメトリクスを収集し、Prometheus/Grafanaで1つの観測基盤に統合する
- 単一のHelmチャート(helm install)でデプロイを完結させ、ダッシュボード作成やスクレイプ設定の手作業を不要にする
- 既存の外部Prometheusインスタンスへメトリクスを転送できる設定を用意し、メトリクス保持・アラートルールを既存監視基盤に集約できるようにする
- GPU種別(Hopper/Blackwell等)でメトリクスをフィルタできるようにし、異種GPUフリートでも利用率を比較可能にする

## 使いどころ

- GPUの割り当てと実利用率のギャップを可視化し、過剰プロビジョニングされたGPUを右サイズ化したいプラットフォームチーム
- Pending状態のGPU podが積み上がるスケジューリングボトルネックを、ユーザーからの障害報告より前に検知したいSRE
- 複数チームで共有する大規模GPUクラスタの利用状況をワークロード単位・namespace単位で把握したい運用担当者
