---
type: guidance
title: GB200 NVL72クラスタ向けSlurmトポロジー認識ジョブスケジューリング
title_original: Unlock Exascale Performance on NVIDIA GB200 NVL72 with Slurm Topology-Aware Job Scheduling
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- cost-optimization
components:
- Slurm
- GB200 NVL72
- NVLink
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/unlock-exascale-performance-on-nvidia-gb200-nvl72-with-slurm-topology-aware-job-scheduling/
published_at: '2026-06-11'
---

## 概要

NVIDIAとSchedMDが共同開発したSlurmのtopology/blockプラグインは、GB200 NVL72のNVLinkドメイン境界を考慮してジョブを配置するトポロジー認識スケジューリングを実現する。5,000ノード規模のクラスタシミュレーションでは、大規模ジョブに16ノード、小規模ジョブに2〜8ノードのセグメントサイズを割り当てる方針により、フラグメンテーションを抑えつつ理論最大値の1%以内までGPU稼働率を高められることが示された。

## 設計のポイント

- ジョブのセグメントサイズをワークロード特性（MoE学習など高I/O要求の大規模ジョブは大きく、小規模ジョブは小さく）に応じて使い分ける。
- 大規模ジョブ（64GPU規模）にはセグメントサイズ16ノードを、小規模ジョブには2〜8ノードを割り当てる方針でNVLinkドメイン境界を最大限活用する。
- フラグメンテーションとセグメントサイズをシミュレーションで継続的にモニタリングし、クラスタ運用中に調整し続ける。

## 使いどころ

- 数千ノード規模のGPUクラスタで複数のAI学習/推論ジョブを共有運用するインフラ運用チーム。
- Mixture-of-Expertsなど高I/O帯域を要する大規模分散学習ジョブをNVLinkドメイン内に収めたい場合。
- ジョブのキュー待ち時間と実行性能のトレードオフを最適化したいクラスタスケジューラ設計者。
