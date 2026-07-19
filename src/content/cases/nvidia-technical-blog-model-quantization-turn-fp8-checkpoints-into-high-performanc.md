---
type: guidance
title: FP8チェックポイントをTensorRT推論エンジンに変換する量子化ワークフロー
title_original: 'Model Quantization: Turn FP8 Checkpoints into High-Performance Inference Engines with NVIDIA TensorRT'
industry: cross-industry
cloud:
- on-prem
patterns:
- model-quantization
- inference-optimization
components:
- NVIDIA TensorRT
- NVIDIA Model Optimizer
- CLIP
- ONNX
- NVIDIA RTX 6000 Ada
- Nsight Deep Learning Designer
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/model-quantization-turn-fp8-checkpoints-into-high-performance-inference-engines-with-nvidia-tensorrt/
published_at: '2026-07-09'
---

## 概要

FP8量子化したCLIPチェックポイントをNVIDIA ModelOptでONNXへエクスポートしTensorRTエンジンへコンパイルするシリーズ完結編。テキストエンコーダで34%、画像エンコーダで50%のファイルサイズ削減を達成しつつ、RTX 6000 Ada上でのプロファイリングではFP16比1.39〜1.45倍の推論レイテンシ改善を確認した。

## 設計のポイント

- 重み側のQuantize+Dequantizeペアを、FP8で保持するDequantizeのみのチェーンに畳み込んでONNXファイルを軽量化する
- TensorRTのエンジンビルド時にQuantizeLinear/DequantizeLinearノードを隣接レイヤーへ融合し、FP8 Tensor Coreで直接実行できるようにする
- Nsight Deep Learning DesignerでONNXグラフ上のFP8境界を可視化しながらプロファイリングし、GEMMやMHAレイヤーでのゲインを確認する

## 使いどころ

- CLIPなどの視覚言語エンコーダをエッジ/ワークステーションGPUで省メモリかつ高速に配信したい開発者
- 量子化チェックポイントを本番のTensorRT推論エンジンへ落とし込む標準的なパイプラインを整備したいMLOpsエンジニア
