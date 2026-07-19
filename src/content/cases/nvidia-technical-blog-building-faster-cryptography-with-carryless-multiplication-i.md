---
type: guidance
title: GPUにキャリーレス乗算命令を実装し暗号処理を最大18.8倍高速化
title_original: Building Faster Cryptography with Carryless Multiplication in NVIDIA CUDA 13.3
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/building-faster-cryptography-with-carryless-multiplication-in-nvidia-cuda-13-3/
published_at: '2026-07-15'
---

## 概要

NVIDIA CUDA 13.3は、x86では15年以上前から存在したキャリーレス乗算命令をNVIDIA Ampere以降の全GPUに追加するPTX命令clmadを導入した。AES-GCMの完全性ハッシュであるGHASHはB200上で従来のビットスライス実装比で最大18.8倍（約6.3TB/s）、ゼロ知識証明で使われるGF(2^128)上のsum-checkプロトコルは3〜13倍高速化するとしている。
