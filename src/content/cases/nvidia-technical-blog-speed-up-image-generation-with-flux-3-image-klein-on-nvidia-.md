---
type: guidance
title: FLUX 3 Image KleinをTensorRT LLM VisualGenでBlackwell向けに高速化
title_original: Speed Up Image Generation with FLUX 3 Image Klein on NVIDIA Blackwell GPUs
company: NVIDIA
industry: media
cloud: []
patterns:
- inference-optimization
- parallel-execution
components:
- TensorRT LLM VisualGen
- FLUX 3 Image Klein
- NVFP4
- FlashInfer
- Cache-DiT
- B200
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/speed-up-image-generation-with-flux-3-image-klein-on-nvidia-blackwell-gpus/
published_at: '2026-11-06'
---

## 概要

画像生成モデルFLUX 3 Image Kleinの推論をNVFP4量子化、融合GEMM、量子化・疎アテンション、ステップキャッシュ、マルチGPU並列で最適化する手順。B200単体でBaseのT2Iが最大3.46倍に、8GPUでは中央値レイテンシが14.9秒から3.0秒に短縮された。

## 設計のポイント

- レイテンシの大半を占めるデノイジングとアテンションに絞って最適化する。
- 品質指標(LPIPS)と速度のトレードオフを見て最適化手法を選ぶ。
- CFG並列とUlysses並列でマルチGPUに分散する。

## 使いどころ

- 画像編集・デザインツールで画像生成の遅延を下げたいチーム。
- Blackwell GPUで拡散モデルを配信する推論基盤。
