---
type: announcement
title: 分子動力学の長距離相互作用をGPUで高速化するNVIDIA cuPotential
title_original: Accelerate Molecular Dynamics Simulations with Accurate, Flexible Primitives Using NVIDIA cuPotential
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
source_url: https://developer.nvidia.com/blog/accelerate-molecular-dynamics-simulations-with-accurate-flexible-primitives-using-nvidia-cupotential/
published_at: '2026-11-13'
---

## 概要

NVIDIA cuPotential は周期境界条件下の静電・分散などの長距離相互作用を評価するモジュール式C APIライブラリで、OpenMM 向けプラグインにより少ない変更で置き換えられる。T4からBlackwellまでのGPUでNPT条件のエンドツーエンドで2〜3倍超の高速化を示し、エネルギードリフトも大幅に低減した。
