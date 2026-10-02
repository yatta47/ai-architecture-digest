---
type: guidance
title: ONNX RuntimeとTensorRT RTXで作るローカルAI推論のC++サンプル集
title_original: Build Local AI Apps with C++ and NVIDIA TensorRT RTX Samples
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
- realtime-transcription
components:
- ONNX Runtime
- NVIDIA TensorRT RTX
- Hugging Face
- OpenAI Whisper
- NVIDIA Parakeet TDT
- NVIDIA Nemotron ASR Streaming
- Meta SAM 2.1
- FLUX.2-klein-4B
- NVIDIA Model Optimizer
- DGX Spark
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/build-local-ai-apps-with-c-and-nvidia-tensorrt-rtx-samples/
published_at: '2026-10-01'
---

## 概要

DIN Deployは、ONNX RuntimeとNVIDIA TensorRT RTX実行プロバイダを組み合わせ、WindowsとLinux上でローカルAI推論をC++で実装するオープンソースのサンプル集である。音声認識、セグメンテーション、画像生成の各サンプルを備え、DGX SparkではCPU比で大幅な高速化（Parakeet TDTで206倍のリアルタイム比、SAM 2.1で38.3 FPS対0.5 FPS）を示している。

## 設計のポイント

- モデルのONNXエクスポート（Python）とデプロイ側（C++ CLI）を分離し、モデル固有ランタイムを不要にする。
- 共通コードはONNX Runtimeのセッション/テンソルAPIに限定し、CUDAなどベンダー固有コードは任意の高速化パスに隔離する。
- ONNXインターフェースを保ったままModel OptimizerでPTQした量子化モデルを、アプリコード変更なしで差し替える。

## 使いどころ

- ネイティブのデスクトップアプリにWhisperなどの音声認識や画像生成をオンデバイスで組み込みたい開発者に向く。
- WindowsとLinux、x86-64とArm64を同一コードベースで扱いたいローカル推論アプリの開発に効く。
