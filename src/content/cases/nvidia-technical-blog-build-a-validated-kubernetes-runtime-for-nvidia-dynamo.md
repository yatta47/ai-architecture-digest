---
type: guidance
title: NVIDIA Dynamoを検証済みレシピでKubernetesに載せる推論基盤構築
title_original: Build a Validated Kubernetes Runtime for NVIDIA Dynamo
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
- gpu-fleet-reliability
components:
- NVIDIA Dynamo
- NVIDIA AI Cluster Runtime (AICR)
- Kubernetes
- Gateway API Inference Extension
- Helmfile
- Prometheus
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/build-a-validated-kubernetes-runtime-for-nvidia-dynamo/
published_at: '2026-10-30'
---

## 概要

AICRはGPUドライバ、DRA、ギャングスケジューリング、ノードヘルス、メトリクスをバージョン固定のレシピにまとめ、Dynamoの実行基盤を再現可能にする。クラスタのスナップショットからレシピ生成、バンドル出力、デプロイ、検証までの5ステップで、アプリ配備前にランタイムを確認できる。

## 設計のポイント

- ランタイム構築とアプリ配備を分離し、検証後にワークロードを載せる。
- コンポーネントのバージョンを固定したレシピで環境差による不具合を防ぐ。
- KVキャッシュイベントを使うキャッシュ対応ルーティングを、Dynamo Frontend経由とGAIE/EPP経由の2経路から選べる。

## 使いどころ

- GPUクラスタ上で分散推論基盤を再現性高く立ち上げたい基盤チーム。
- 共有のKubernetes Ingressに推論エンドポイントを統合したい組織。
