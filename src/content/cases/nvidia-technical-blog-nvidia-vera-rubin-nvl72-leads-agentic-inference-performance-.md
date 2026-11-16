---
type: announcement
title: MLPerf Endpoints v1.0でVera Rubin NVL72がエージェント推論でGB300の10倍超のkWあたり処理量
title_original: NVIDIA Vera Rubin NVL72 Leads Agentic Inference Performance on MLPerf Endpoints v1.0
company: NVIDIA
industry: cross-industry
cloud:
- multi-cloud
patterns:
- inference-optimization
- gpu-fleet-reliability
components:
- NVIDIA Vera Rubin NVL72
- NVIDIA GB300 NVL72
- NVIDIA Dynamo
- Kimi K3
- DeepSeek-V4.1-Flash
- Qwen3.6-35B-A3B
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-leads-agentic-inference-performance-on-mlperf-endpoints-v1-0/
published_at: '2026-11-16'
---

## 概要

暫定結果として、Vera Rubin NVL72は50 tokens/sec/userの対話性でGB300 NVL72の10倍超のkWあたりスループットを示した。プレフィックスキャッシュ、状態再利用、Dynamoルーティングなど、エージェント負荷向けの配信最適化も解説する。

## 設計のポイント

- 長い履歴と tool call が続くエージェント負荷に合わせ、プレフィックスキャッシュと状態再利用で重複計算を減らす
- Dynamoルーティングで配信負荷を分散する
- モデル固有のGPUカーネル最適化やマルチトークン予測で逐次デコードを減らす
- tool call検証で高速化が品質を損なわないことを確認する

## 使いどころ

- エージェント推論基盤の容量・電力計画
- GPU世代選定の比較材料
