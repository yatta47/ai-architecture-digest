---
type: announcement
title: 'CCCL Runtime: CUDA向けのモダンC++ランタイム'
title_original: 'CCCL Runtime: A Modern C++ Runtime for CUDA'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/cccl-runtime-a-modern-c-runtime-for-cuda/
published_at: '2026-07-09'
---

## 概要

CUDA 13.2から提供されるCCCL runtimeは、stream・メモリ確保・カーネル起動などCUDAの基本概念を現代的なC++イディオムで表現し直す新しいAPI群。所有型と非所有型(_ref)の区別や明示的な依存関係の記述により、暗黙のグローバル状態に依存しがちな従来のCUDA Runtime APIより安全で合成しやすい設計になっている。
