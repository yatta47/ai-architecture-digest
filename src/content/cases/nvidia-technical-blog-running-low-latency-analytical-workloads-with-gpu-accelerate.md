---
type: case
title: 'GPU上のPresto: GB200 NVL72で低レイテンシ分析クエリを実現'
title_original: Running Low-Latency Analytical Workloads with GPU-Accelerated Presto on NVIDIA GB200 NVL72
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
source_url: https://developer.nvidia.com/blog/running-low-latency-analytical-workloads-with-gpu-accelerated-presto-on-nvidia-gb200-nvl72/
published_at: '2026-07-09'
---

## 概要

分散SQLエンジンPrestoをNVIDIA cuDFとNVLinkでGPU化し、DGX B200やGB200 NVL72上でTPC-H由来のベンチマークを実行した事例。IBM Storage ScaleとGPUDirect Storageを組み合わせたI/O最適化により、CPUクラスタ比で最大8倍の低レイテンシと64%の追加高速化を達成した。
