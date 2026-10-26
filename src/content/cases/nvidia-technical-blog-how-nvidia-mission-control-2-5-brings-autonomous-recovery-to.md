---
type: announcement
title: KubernetesとRun:ai上のAIジョブに自律復旧を広げるMission Control 2.5
title_original: How NVIDIA Mission Control 2.5 Brings Autonomous Recovery to Kubernetes
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- decision-execution
- root-cause-analysis
components:
- NVIDIA Mission Control
- NVIDIA Run:ai
- Kubernetes
- Slurm
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-nvidia-mission-control-2-5-brings-autonomous-recovery-to-kubernetes/
published_at: '2026-10-24'
---

## 概要

NVIDIA Mission Control 2.5は、従来Slurmのワークロード向けだった自律復旧エンジンを、Run:aiが管理するKubernetesワークロードへ拡張した。スケジューラ、ジョブ復旧、ハードウェア復旧の3層の制御ループで、故障の分類、ノードの隔離と診断、ジョブの再開を自動化する。

## 設計のポイント

- スケジューラによる配置、ジョブ文脈による障害分類、ハードウェアの隔離と診断を3層に分け、協調させる。
- ハードウェア故障では、ジョブの再起動や再配置とノードの隔離および診断を並行して進める。
- 一過性のソフトウェアエラーはジョブの再試行にとどめ、不要なハードウェア対処を避ける。
- 劣化を早期に検知し、ジョブが止まる前にリスクのあるノードをスケジューリング対象から外す。

## 使いどころ

- 数百ノード規模の分散学習を共有クラスタで長期間動かすAIファクトリーの運用チーム。
- 手動対応や静的チェックポイントに頼った障害対応を減らしたい場面。
