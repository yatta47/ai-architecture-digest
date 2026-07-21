---
type: guidance
title: C++でタイルベースGPUカーネルを書くCUDA Tile C++
title_original: Develop High-Performance GPU Kernels in C++ with NVIDIA CUDA Tile
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/develop-high-performance-gpu-kernels-in-cpp-with-nvidia-cuda-tile/
published_at: '2026-06-11'
---

## 概要

NVIDIAはCUDA 13.3で、タイルベースのGPUプログラミングモデルをC++に拡張したCUDA Tile C++を公開した。tensor_spanやpartition_viewといった抽象化により、スレッドやメモリ移動を明示的に管理せずに高性能なGPUカーネルをC++で記述でき、既存の大規模C++コードベースにも組み込みやすい。ベクトル加算や行列積の例を通じて、従来のSIMTカーネルより宣言的かつアーキテクチャ間で移植性の高いカーネル記述が可能になることを示している。
