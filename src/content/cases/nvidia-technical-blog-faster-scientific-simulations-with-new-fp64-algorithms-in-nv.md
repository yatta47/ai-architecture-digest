---
type: announcement
title: cuBLASの新FP64アルゴリズム(Ozaki-II, 2M)で科学計算のGEMMを高速化
title_original: Faster Scientific Simulations with New FP64 Algorithms in NVIDIA cuBLAS
ai_relevant: false
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns: []
components: []
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/faster-scientific-simulations-with-new-fp64-algorithms-in-nvidia-cublas/
published_at: '2026-11-13'
---

## 概要

CUDA Toolkit 13.4.2のcuBLASに、整数Tensor CoreでFP64精度を保ったままDGEMM/ZGEMMを高速化するOzaki-IIと2Mが追加された。DGEMMはVR NVL72で最大5.5倍、量子化学や材料科学のシミュレーションでも高速化を示す。
