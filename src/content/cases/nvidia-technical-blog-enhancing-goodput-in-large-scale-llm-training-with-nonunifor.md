---
type: guidance
title: 'Nonuniform Tensor Parallelism: GPU障害時もLLM学習のGoodputを維持'
title_original: Enhancing Goodput in Large-Scale LLM Training with Nonuniform Tensor Parallelism
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- parallel-execution
- llmops
components:
- NVIDIA NVLink
- NVIDIA Blackwell
- NVIDIA Blackwell Ultra
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/enhancing-goodput-in-large-scale-llm-training-with-nonuniform-tensor-parallelism/
published_at: '2026-07-09'
---

## 概要

数千GPU規模のLLM学習では一時的なGPU不調がTPグループ全体を停滞させGoodputを損なう。Nonuniform Tensor Parallelism(NTP)はGPU脱落時にTP次数を動的に縮小しつつ電力ブーストで性能を補い、1%未満のオーバーヘッドでスケールアップドメイン内の一部障害を吸収する。

## 設計のポイント

- TPグループの一部GPUが停止した場合、残ったGPUだけでTP次数を自動的に縮小して計算を継続する
- 縮小によるスループット低下を、ラック設計上の電力・冷却余裕を使った動的パワーブーストで補償する
- テンソルの再シャーディングをオーバーラップ実行し導入オーバーヘッドを1%未満に抑える

## 使いどころ

- 72GPU規模のNVLinkスケールアップドメインで学習ジョブを運用しGPU不調による全体停止を避けたいAIインフラチーム
- データ並列レプリカ単位でのチェックポイント再起動よりきめ細かい耐障害性が必要な大規模学習基盤
