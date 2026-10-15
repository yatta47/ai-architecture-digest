---
type: guidance
title: AI Runtime上のQwen微調整を6倍高速化した性能分析
title_original: Reducing Qwen training time by 6x on AI Runtime
company: Databricks
industry: cross-industry
cloud: []
patterns:
- fine-tuning
- inference-optimization
- gpu-fleet-reliability
components:
- Databricks AI Runtime
- Qwen
- FSDP2
- PyTorch
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/reducing-qwen-training-time-6x-ai-runtime
published_at: '2026-10-14'
---

## 概要

GPU使用率が98%でも実効利用は低い点に着目し、torchトレースで分析してカーネル導入とデータパイプライン改善を行った。Qwen 27Bの微調整を7時間44分から1時間17分へ短縮した。

## 設計のポイント

- GPU使用率ではなくトレースで実際の利用状況を測る
- FSDP2と活性化チェックポイントでメモリに収める
- カーネルとデータパイプラインを順に改善する

## 使いどころ

- 大規模モデルの学習時間とGPU費用を減らしたい基盤チーム
