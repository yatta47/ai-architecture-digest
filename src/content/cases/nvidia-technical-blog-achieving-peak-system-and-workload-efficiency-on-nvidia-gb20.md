---
type: guidance
title: SlurmブロックスケジューリングによるGB200 NVL72ラックスケールGPUクラスタの性能最適化
title_original: Achieving Peak System and Workload Efficiency on NVIDIA GB200 NVL72 with Slurm Block Scheduling
company: NVIDIA, SchedMD
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-cluster-scheduling
- parallel-execution
- gpu-fleet-reliability
- cost-optimization
components:
- Slurm
- topology/block
- NVIDIA GB200 NVL72
- GB300 NVL72
- NVIDIA IMEX
- NVLink
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/achieving-peak-system-and-workload-efficiency-on-nvidia-gb200-nvl72-with-slurm-block-scheduling/
published_at: '2026-06-11'
---

## 概要

GB200 NVL72はラック全体にNVLinkコヒーレントメモリドメインを広げ130TB/sの帯域を実現するが、ドメイン境界を越える通信は急激に性能が落ちるため、NVIDIAとSchedMDはSlurmにtopology/blockプラグインと--segment引数を導入し、NVLinkドメインを剛体的なスケジューリング単位「ブロック」として扱うようにした。これによりジョブのフラグメンテーションを防ぎつつ、Tensor ParallelismやExpert Parallelismなどアプリケーション固有のNVLink局所性要件に応じてセグメントサイズを調整できるようになった。

## 設計のポイント

- NVLinkドメイン境界をベストエフォートではなくハードな制約としてスケジューラに認識させ、topology/blockプラグインでブロック単位のジョブ配置を行う
- --segment引数でジョブが要求するNVLink局所性の粒度を明示的に指定でき、スケジューラ効率とハードウェア局所性要件のトレードオフを調整できる
- Tensor Parallelismには小さく密なセグメント、Expert Parallelismには大きなセグメントを使うなど、並列化手法に応じてセグメントサイズを使い分ける
- incomplete blockのサポートやNVIDIA IMEXによるドライバレベルのGPUメモリ分離など高度な機能でラックスケール運用の最適化と一貫した高性能を維持する

## 使いどころ

- GB200/GB300 NVL72のようなラックスケールNVLinkドメインを持つクラスタで大規模モデルの学習ジョブを運用するチーム
- ジョブのフラグメンテーションによるキュー待ち時間増加や性能劣化を避けたいクラスタ管理者
- Tensor ParallelismとExpert Parallelismが混在する学習ワークロードでNVLink局所性要件を細かく制御したい場合
