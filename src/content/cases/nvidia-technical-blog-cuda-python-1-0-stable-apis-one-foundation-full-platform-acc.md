---
type: announcement
title: CUDA Python 1.0がPythonからCUDAプラットフォーム全体への公式な統一アクセスを提供
title_original: 'CUDA Python 1.0: Stable APIs, One Foundation, Full Platform Access'
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
source_url: https://developer.nvidia.com/blog/cuda-python-1-0-stable-apis-one-foundation-full-platform-access/
published_at: '2026-08-24'
---

## 概要

NVIDIAはCUDA 13.3と同時にCUDA Python 1.0をリリースし、cuda.core・cuda.compute・cuda.bindings・nvmath-python・cuda-pathfinderといった公式ライブラリ群を単一の基盤の上に統一した。セマンティックバージョニングによりAPIの安定性と非推奨計画を保証し、異なるPython GPUライブラリが同じCUDAオブジェクト（デバイス・ストリーム・バッファ）を共有してコピー無しで連携できるようにする。
