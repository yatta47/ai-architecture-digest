---
type: announcement
title: 198BパラメータのマルチモーダルVLM「Step 3.7 Flash」をNVIDIA基盤で本番展開
title_original: Run Step 3.7 Flash on NVIDIA GPUs with Enterprise-Ready Multimodal AI
industry: cross-industry
cloud: []
patterns:
- ai-agent
- inference-optimization
- fine-tuning
components:
- Step 3.7 Flash
- NVIDIA NIM
- NVIDIA TensorRT-LLM
- vLLM
- SGLang
- NVIDIA NeMo
- NVIDIA DGX Station
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/run-step-3-7-flash-on-nvidia-gpus-with-enterprise-ready-multimodal-ai/
published_at: '2026-06-11'
---

## 概要

StepFunの198BパラメータMixture-of-ExpertsビジョンランゲージモデルStep 3.7 Flash(アクティブ11B、256kコンテキスト)を、NVIDIA NIMでコンテナ化された本番推論マイクロサービスとしてオンプレ・クラウド・ハイブリッドに展開できるようにした。NVFP4量子化チェックポイントによる推論高速化に加え、NeMo AutomodelによるHugging Faceチェックポイントからの変換不要なDay 0ファインチューニング(SFT/LoRA)にも対応する。

## 設計のポイント

- SGLang・TensorRT-LLM・vLLMなど複数のOSS推論フレームワークに対応させ、NVIDIA最適化カーネルをそのまま使えるようにする
- NVFP4量子化チェックポイントでメモリ帯域と保存容量を削減し推論を高速化する
- NeMo Automodelがチェックポイント変換なしにHugging Faceモデルから直接Day 0でSFT/LoRAファインチューニングできるようにする

## 使いどころ

- 画像・動画・文書を横断する知覚・検索・多段推論をエンタープライズ規模で行いたいチーム
- オンプレ・クラウド・ハイブリッドを問わず同一のNIMコンテナで本番展開したいプラットフォームチーム
