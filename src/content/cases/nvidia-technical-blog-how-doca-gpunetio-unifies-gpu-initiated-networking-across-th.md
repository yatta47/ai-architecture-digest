---
type: guidance
title: DOCA GPUNetIOによるGPU主導ネットワークの統一
title_original: How DOCA GPUNetIO Unifies GPU-Initiated Networking Across the NVIDIA Software Stack
ai_relevant: false
company: NVIDIA
industry: other
cloud: []
patterns: []
components: []
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/doca-gpunetio-gda-ki-unified-gpu-networking/
published_at: '2026-10-06'
---

## 概要

DOCA GPUNetIOは、CUDAカーネルがCPUを介さずEthernetやRDMAを直接操作する基盤を提供する。NCCL、NVSHMEM、UCX/NIXLなどの通信ライブラリが個別実装をやめて共通基盤に載り始めた。
