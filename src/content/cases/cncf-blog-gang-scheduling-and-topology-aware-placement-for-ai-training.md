---
type: guidance
title: KueueとCoschedulingによるAI学習向けギャング・トポロジー認識スケジューリング
title_original: Gang scheduling and topology-aware placement for AI training in Kubernetes
company: Datadog
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- parallel-execution
components:
- Kubernetes
- Kueue
- Coscheduling plugin
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/11/12/gang-scheduling-and-topology-aware-placement-for-ai-training-in-kubernetes/
published_at: '2026-11-12'
---

## 概要

分散AI学習ではPodの同時起動とGPU間帯域に合った配置が必要だが、標準Kubernetesスケジューラは個別配置のため満たせない。KueueとCoschedulingでギャングスケジューリングとトポロジー認識配置を行い、GPUの遊休と性能低下を防ぐ方法を解説する。

## 設計のポイント

- 全Podを同時に起動するギャングスケジューリングで、部分起動によるGPU遊休を避ける。
- GPU間のインターコネクト階層を考慮して配置し通信性能を引き出す。
- 検証手順でスケジューリング挙動を確認してから運用する。

## 使いどころ

- KubernetesでGPUクラスタを共有運用する基盤チーム。
- 大規模分散学習のGPU稼働率を上げたい組織。
- GPU費用の無駄を抑えたいFinOps担当。
