---
type: guidance
title: VRAM 12GBのローカルGPUで世界基盤モデルCosmos 3 Nanoを動かすオフロード手法
title_original: How to Run NVIDIA Cosmos 3 on Local AI Devices Using Hugging Face Diffusers
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
components:
- NVIDIA Cosmos 3 Nano
- Hugging Face Diffusers
- Cosmos-Framework
- PyTorch
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-to-run-nvidia-cosmos-3-on-local-ai-devices-using-hugging-face-diffusers/
published_at: '2026-11-24'
---

## 概要

重みをシステムRAMに置き必要な分だけGPUへ転送することで、VRAM 12GBでも動画生成モデルCosmos 3 Nanoを実行する手順。FP8チェックポイントでさらにピークメモリを削減できるが、対話的な低遅延は得られない。

## 設計のポイント

- 重みの保管先をシステムRAMにし、transformerブロック単位でGPUへ転送してVRAM要件を下げる（RAMとPCIe帯域が代償）。
- 条件入力が固定なら理解側の計算結果を一度だけ作り、デノイズの各ステップで再利用する。
- アテンションはBF16を保つネイティブ混合精度のFP8で品質とメモリを両立する。

## 使いどころ

- 手元の消費者向けGPUでフィジカルAI用の動画生成を試したい開発者。
- VRAM制約下で大きなモデルを動かす推論構成を検討する人。
