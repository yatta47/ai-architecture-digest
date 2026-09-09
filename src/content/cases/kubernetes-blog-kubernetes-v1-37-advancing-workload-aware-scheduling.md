---
type: announcement
title: Kubernetes v1.37のワークロード対応スケジューリング強化とギャングスケジューリングのBeta昇格
title_original: 'Kubernetes v1.37: Advancing Workload-Aware Scheduling'
industry: cross-industry
cloud: []
patterns:
- gpu-fleet-reliability
components:
- Kubernetes
- Workload API
- PodGroup API
- CompositePodGroup API
- JobSet
- LeaderWorkerSet
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/09/08/kubernetes-v1-37-advancing-workload-aware-scheduling/
published_at: '2026-09-08'
---

## 概要

Kubernetes v1.37は、AI/MLや大規模バッチワークロード向けのWorkload-Aware Scheduling（WAS）を前進させ、WorkloadとPodGroup APIによるギャングスケジューリングやWorkload-Aware Preemption、PodGroup単位のDRA ResourceClaim共有をBetaへ昇格させた。多階層のトポロジ制約を表現できるCompositePodGroup APIも新設し、JobSetやLeaderWorkerSetのような高次拡張APIをネイティブにスケジューリングできるようにする。

## 設計のポイント

- 個々のPodではなくPodGroupを単位としてキューイング・プリエンプションすることでall-or-nothingなギャングスケジューリングを実現する
- minCountを可変にし弾力的ワークロードが稼働中のPodを止めずに必要最小サイズを増減できるようにする
- CompositePodGroupで階層構造を表現しスケジューラが階層全体を1つのスケジューリング単位として扱えるようにする
- プリエンプションはPodGroup全体のdisruptionModeを尊重し単一Pod単位の破壊的な退去を防ぐ

## 使いどころ

- 分散学習やLLM推論など複数Podが揃って初めて意味を持つAI/MLワークロードをKubernetes上で運用するチーム
- JobSetやLeaderWorkerSetのような上位コントローラを使い分散トレーニングジョブを組んでいる基盤担当者
- GPUなど高価な共有リソースでバッチジョブのプリエンプションと弾力的なスケーリングを両立させたい運用者
