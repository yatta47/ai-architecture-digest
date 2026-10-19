---
type: opinion
title: AIワークロードがKubernetesのスケジューラとオートスケーラの分担を変える
title_original: How AI workloads are reshaping Kubernetes autoscaling
company: AWS
industry: cross-industry
cloud:
- multi-cloud
patterns:
- cost-optimization
components:
- Kubernetes
- Karpenter
- Cluster Autoscaler
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/10/19/how-ai-workloads-are-reshaping-kubernetes-autoscaling/
published_at: '2026-10-19'
---

## 概要

Kubernetesでは、スケジューラがPodを既存ノードに置き、オートスケーラがノードを足すという分業が長く機能してきた。AIアクセラレータでは、追加されるノードの形がスケジューラの要求に合わず、容量があってもPodがPendingのままになる問題が出る。予約容量やトポロジなどの課題へのコミュニティの対応と、オートスケーラがスケジューラを意識した方向へ進む見通しを述べている。

## 設計のポイント

- ノードを追加するか否かだけでなく、そのノードが仕事に適した形かを判断する必要がある。
- 予約済み容量から起動するノードかどうかを、スケールアップ時に考慮する。
- デバイス間の接続関係(トポロジ)や同一NUMAドメインの局所性を、スケジューラとオートスケーラで共有する。

## 使いどころ

- GPUクラスタでPodがPendingのまま高価なアクセラレータが遊んでいる場面。
- 容量予約を併用してAI基盤のコストを管理するプラットフォームチーム。
- Kubernetes上のAI基盤の将来動向を把握したい場面。
