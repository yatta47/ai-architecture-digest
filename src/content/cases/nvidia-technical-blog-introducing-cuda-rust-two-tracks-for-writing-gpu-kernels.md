---
type: announcement
title: 'GPUカーネルをRustで書く2つの新トラック: cuda-oxideとcutile-rs'
title_original: 'Introducing CUDA Rust: Two Tracks for Writing GPU Kernels'
ai_relevant: false
company: NVIDIA
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/
published_at: '2026-09-04'
---

## 概要

NVIDIAが、GPUカーネルをRustでネイティブに書ける2つのトラックを発表。SIMTモデル向けのcuda-oxideはPTXへ直接コンパイルし、Tileモデル向けのcutile-rsは安定版Rustで動作する。両者ともコンパイル時にメモリ安全性を保証し、cutile-rsは既にHuggingFaceの推論エンジンGroutやmistral.rsで採用されている。
