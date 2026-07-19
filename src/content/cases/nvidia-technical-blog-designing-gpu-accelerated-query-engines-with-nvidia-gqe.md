---
type: guidance
title: 'GQE: NVIDIA GPUで作るGPU高速SQLクエリエンジン'
title_original: Designing GPU-Accelerated Query Engines with NVIDIA GQE
ai_relevant: false
industry: cross-industry
cloud:
- on-prem
patterns: []
components: []
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/designing-gpu-accelerated-query-engines-with-nvidia-gqe/
published_at: '2026-07-09'
---

## 概要

GQEはHBMやNVLink-C2C、GB200 NVL4の専用解凍エンジンを活用してCPU-GPU間のデータ移動・圧縮・パーティションプルーニングを最適化するSQLクエリエンジンのリファレンスアーキテクチャ。TPC-H SF1000ベンチマークで既存CPUデータベース比7.5倍、クエリ単位で最大25.5倍の高速化を達成した。
