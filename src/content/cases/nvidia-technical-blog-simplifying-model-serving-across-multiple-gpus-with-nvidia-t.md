---
type: guidance
title: TensorRTマルチデバイス推論でGPU分散サービングを単一エンドポイントに集約
title_original: Simplifying Model Serving Across Multiple GPUs with NVIDIA TensorRT Multi-Device Integration in NVIDIA Dynamo-Triton
industry: media
cloud: []
patterns:
- inference-optimization
- parallel-execution
components:
- NVIDIA TensorRT
- NVIDIA Dynamo-Triton
- NVIDIA Cosmos 3 Nano
- NCCL
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/simplifying-model-serving-across-multiple-gpus-with-nvidia-tensorrt-multi-device-integration-in-nvidia-dynamo-triton/
published_at: '2026-09-21'
---

## 概要

NVIDIA Dynamo-Triton（旧Triton Inference Server）のTensorRTバックエンドがマルチデバイス推論に対応し、1つのKIND_MODELインスタンスが複数GPUを保有して単一のgRPCエンドポイントを公開できるようになった。Cosmos 3 Nanoの動画生成にUlysses文脈並列を適用したデモでは、1GPUの156.6秒から8GPUの34.2秒までエンドツーエンドの生成レイテンシを短縮した。

## 設計のポイント

- 分散推論グラフを事前にTensorRTプランへコンパイルしクライアントはランクの調整を意識せず単一のgRPC呼び出しで済む
- Ulysses文脈並列で注意機構のパーティション軸を変え各ランクが動画トークン列の一部ヘッドを全区間処理する構成にした
- アプリケーション側（Diffusers）はプロンプト・スケジューリング・後処理のオーケストレーションのみ担当し変更不要にした
- GPU数を2/4/8と増やす際もconfig.pbtxtのパラメータ変更のみで多重度を切り替えられる

## 使いどころ

- 単一GPUのメモリ・演算能力を超える大規模な生成動画・画像トランスフォーマーを配信したいチーム
- クライアントアプリのオーケストレーションコードを変えずにGPUスケールを調整したい推論基盤
- レイテンシ短縮によりレビュー・再生成のサイクルを速めたい生成メディアワークフロー
