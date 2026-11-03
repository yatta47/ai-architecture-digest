---
type: guidance
title: NVIDIA Attribution：分散AIワークロード障害をログ・メトリクスから根本原因特定
title_original: Diagnose Distributed AI Workload Failures with NVIDIA Attribution
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- root-cause-analysis
- gpu-fleet-reliability
components:
- NVIDIA Attribution
- Slurm
- Kueue
- Loki
- PromQL
- NCCL
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/diagnose-distributed-ai-workload-failures-with-nvidia-attribution/
published_at: '2026-11-02'
---

## 概要

NVIDIA Attributionはワークロード単位のログ・メトリクス・スケジューラ状態を相関し、結果・根本原因・影響ノード・証拠を含む構造化診断を返すオープンソースツール。NVIDIA社内で週数百万ワークロードを解析している。

## 設計のポイント

- スコープ化、観測収集、決定論的ルールでの相関、構造化結果の4段階で診断する
- 根本原因（NVLink信号品質）と下流症状（NCCLエラー）を分けて保持する
- Slurm/Kueue/Loki等のコネクタで既存環境に接続する参照オーケストレータを提供

## 使いどころ

- 大規模GPUクラスタの障害調査を自動化したい運用者
- 学習ジョブ失敗の原因切り分けを再現可能にしたいチーム
