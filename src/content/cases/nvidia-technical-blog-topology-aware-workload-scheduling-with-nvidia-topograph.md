---
type: guidance
title: クラスタのネットワークトポロジーを自動検出しAIワークロード配置を最適化するTopograph
title_original: Topology-Aware Workload Scheduling with NVIDIA Topograph
industry: cross-industry
cloud:
- multi-cloud
patterns:
- gpu-fleet-reliability
- cost-optimization
components:
- NVIDIA Topograph
- Kubernetes
- Slurm
- NVIDIA NVLink
- Slinky
- KAI Scheduler
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/topology-aware-workload-scheduling-with-nvidia-topograph/
published_at: '2026-09-22'
---

## 概要

GPUクラスタの配置がトポロジーの局所性を無視すると帯域を食い合いスループット低下やコスト増につながる。NVIDIA Topographはクラウドのオンプレミスのファブリック情報を正規化された共通モデルに変換し、Kubernetesノードラベル・Slurm設定・Slinky ConfigMapとして出力することでスケジューラが常に最新のトポロジー情報に基づき配置できるようにする。

## 設計のポイント

- providerがクラウド/オンプレミスのトポロジーを検出しengineがKubernetes/Slurm向けの形式に変換する疎結合な2層構成にした
- クラスタの変更を監視して自動的にトポロジービューを再生成し手動メンテナンスを不要にした
- KAI Schedulerと連携しトポロジーを考慮したギャングスケジューリングをAIファクトリー全体で実現する
- 対応クラウド（Google Cloud、Lambda、Nebius、Nscale、OCI）とオンプレミス（InfiniBand、Spectrum-X、MNNVL）を同じモデルで扱う

## 使いどころ

- 大規模な分散学習・推論クラスタで通信局所性を無視した配置によりGPUが遊んでいるケース
- 複数クラウド・オンプレミスにまたがるGPUクラスタで一貫したスケジューリング方針を持ちたい場合
- KubernetesとSlurmを併用する環境でトポロジー情報を二重管理したくないプラットフォームチーム
