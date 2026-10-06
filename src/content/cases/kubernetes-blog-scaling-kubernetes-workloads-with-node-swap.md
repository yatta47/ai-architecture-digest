---
type: case
title: ノードSwapでエージェント系ワークロードのPod密度を高める
title_original: Scaling Kubernetes Workloads with Node Swap
company: Kubernetes
industry: cross-industry
cloud:
- multi-cloud
patterns:
- cost-optimization
- parallel-execution
components:
- Kubernetes
- agent-sandbox
- NVMe SSD
outcome:
  type: cost
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/10/05/scaling-kubernetes-workloads-with-node-swap/
published_at: '2026-10-05'
---

## 概要

Kubernetes 1.34でGAとなったノードSwapをNVMe SSDで支え、休止中のメモリを退避させてPod密度を上げる検証。CI/CDカーネルビルド、サンドボックス化ブラウザ、隔離Pythonランタイムで最大3倍の密度向上を、遅延への影響を小さく確認した。

## 設計のポイント

- エージェントの休止メモリをSwapに逃がして、ノード当たりのPod数を増やす。
- cgroup v2でSwap上限を独立管理できる前提で運用する。
- 3種類のワークロードで密度と遅延のトレードオフを実測して導入判断する。

## 使いどころ

- サンドボックス型エージェントを大量に動かす基盤チーム。
- メモリが先に尽きるクラスタのコスト削減。
