---
type: announcement
title: NVIDIA BlueField-4によるエージェントAIファクトリーのインフラ最適化
title_original: Scaling Agentic AI Factories Through Extreme Co-Design with NVIDIA BlueField
industry: cross-industry
cloud: []
patterns:
- gpu-fleet-reliability
- inference-optimization
- reasoning-computation-separation
- memory-consolidation
components:
- NVIDIA BlueField-4
- Vera BlueField-4 STX
- NVIDIA DOCA
- NVIDIA Vera Rubin
- NVIDIA Grace CPU
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/scaling-agentic-ai-factories-through-extreme-co-design-with-nvidia-bluefield/
published_at: '2026-07-13'
---

## 概要

エージェントAIによる推論はGPU/CPU/メモリ/ネットワーク/ストレージ/セキュリティにまたがる分散ワークフローとなり、KVキャッシュなどコンテキストの移動・保護・再利用がインフラの一部になる。NVIDIA BlueField-4 DPUとVera BlueField-4 STX、DOCAソフトウェアがこれらの処理をホストCPUからオフロードし、GPU使用率向上・レイテンシ予測性・テナント分離・トークン単価低減を実現する。

## 設計のポイント

- ネットワーキング・ストレージ・セキュリティ・テレメトリ・コンテキスト管理をDPU/ストレージプロセッサにオフロードし、ホストCPUとGPUを推論本体に専念させる。
- KVキャッシュの配置・保護・再利用を推論に付随するものではなくインフラのデータパスの一部として明示的に設計する。
- DOCAで機能横断のプログラマブルなソフトウェア基盤を提供し、KVキャッシュ再利用・テナント分離・ゼロトラストセキュリティを統一的に実装する。

## 使いどころ

- 大規模なマルチテナントAIファクトリーを運用しGPU使用率とトークン単価を最適化したいインフラチーム。
- 長いコンテキストやエージェント的推論でKVキャッシュ管理がボトルネックになっている運用者。
