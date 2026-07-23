---
type: opinion
title: AIインフラの未来はコミュニティ主導のオープンな基盤で作られる
title_original: The future of AI is community-driven and open
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- gpu-fleet-reliability
components:
- Kubernetes
- NVIDIA GPU Operator
- DRA Driver
- KAI Scheduler
- NVIDIA Container Toolkit
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/23/the-future-of-ai-is-community-driven-and-open/
published_at: '2026-07-23'
---

## 概要

NVIDIAのシニアディレクターが、KubernetesをAIワークロードの標準基盤に育てるための取り組みを解説する。GPU Dynamic Resource Allocation(DRA)ドライバのアップストリーム化、KAIスケジューラのCNCF Sandbox入り、Kubernetes AI Conformance Programの拡大など、NVIDIAがCNCFガバナンスボードに参加し3年間で400万ドルを投じてGPUを第一級リソースとしてKubernetesに統合する方針を述べる。

## 設計のポイント

- 静的なGPU割り当てをDRA(Dynamic Resource Allocation)によるリアルタイム・オンデマンド割り当てに置き換える
- Multi-Node NVLink経由でノードをまたいでGPUメモリを安全に共有するComputeDomainsを導入する
- ガング・スケジューリングと階層キュー(Dominant Resource Fairness)で大規模GPUクラスタのスケジューリング要求に対応する
- AI Conformance ProgramでAI対応基盤がプロバイダ間で一貫して動作することを検証する

## 使いどころ

- 大規模GPUクラスタでマルチテナントのトレーニング/推論を運用するプラットフォームチーム
- GPUリソースの静的予約による過剰プロビジョニングを解消したいインフラ担当者
- ベンダーロックインを避けオープンな標準に沿ったAIインフラを構築したい組織
