---
type: case
title: 機械学習原子間ポテンシャルのTensor Core高速化
title_original: Unlocking Tensor Core Performance for Machine Learning Interatomic Potentials
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
source_url: https://developer.nvidia.com/blog/unlocking-tensor-core-performance-for-machine-learning-interatomic-potentials/
published_at: '2026-10-29'
---

## 概要

機械学習原子間ポテンシャルの推論で、FP32行列積をTensor Coreの低精度演算に分解するBF16x9やTF32x3を使い、精度を保ったまま高速化した。分子動力学ステップ全体で最大1.5倍の高速化が報告されている。
