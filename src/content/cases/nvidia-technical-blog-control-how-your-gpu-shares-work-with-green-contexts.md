---
type: guidance
title: CUDA Green ContextsによるGPU実行リソースの分割
title_original: Control How Your GPU Shares Work with Green Contexts
ai_relevant: false
company: NVIDIA
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/control-how-your-gpu-shares-work-with-green-contexts/
published_at: '2026-10-05'
---

## 概要

CUDA 13.1のGreen Contextsで、プロセス内のSM等のGPU実行リソースを明示的に分割できる。遅延に敏感なカーネルに専用SMを割り当て、Blackwell GPUで重要カーネル遅延を0.140msから0.007msに短縮した。
