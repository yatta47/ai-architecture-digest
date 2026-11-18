---
type: announcement
title: NVIDIA Daviator：VASPのk点バッチ処理と混合精度でDFTを高速化
title_original: Tackling GPU bottlenecks in plane-wave DFT with k-point batching and mixed precision
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
source_url: https://developer.nvidia.com/blog/tackling-gpu-bottlenecks-in-plane-wave-dft-with-k-point-batching-and-mixed-precision/
published_at: '2026-11-17'
---

## 概要

NVIDIAのDaviatorは、VASPのk点逐次処理をバッチ化したGPUカーネルに置き換え、CPU比で最大22倍高速、最大75%低コストを達成した。FP32とFP64を使い分ける混合精度で約2倍の追加高速化も得られる。
