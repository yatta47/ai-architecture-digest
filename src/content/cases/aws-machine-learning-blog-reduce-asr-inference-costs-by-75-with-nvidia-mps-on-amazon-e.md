---
type: case
title: 臨床音声AIのGPU台数を75%削減したCUDA MPS活用
title_original: Reduce ASR inference costs by 75% with NVIDIA MPS on Amazon EC2
company: Heidi Health
industry: healthcare
cloud:
- aws
patterns:
- inference-optimization
- cost-optimization
components:
- Amazon EC2
- NVIDIA CUDA MPS
- NVIDIA Triton Inference Server
- NVIDIA Parakeet TDT 0.6B V2
- ONNX Runtime
- TensorRT
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/reduce-asr-inference-costs-by-75-with-nvidia-mps-on-amazon-ec2/
published_at: '2026-08-27'
---

## 概要

週2.4百万件の臨床診療を処理するHeidi Healthは、NVIDIA CUDA MPSとTriton Inference ServerをAmazon EC2のGPUインスタンス上で組み合わせ、ASR推論のGPU使用率を改善した。サブ秒レイテンシを維持したまま、必要GPUインスタンス数を16台から4台へ75%削減した。

## 設計のポイント

- CUDA MPSで1枚のGPUを複数プロセスに論理分割し、デフォルトのタイムスライシングで生じるコンテキストスイッチのオーバーヘッドと約80%のGPUアイドルを解消
- 転写処理は25%SM×4プロセス、話者分離処理は12%SM×8プロセスと、ワークロード特性ごとに異なるMPSパーティションサイズを割り当て
- 計算負荷の高いConformerエンコーダはONNX Runtime＋TensorRTでFP16化し、可変長生成のRNN-TデコーダはPyTorch CUDAネイティブのまま残すハイブリッド構成
- TritonのモデルインスタンスをMPSパーティションに1対1で対応させ、動的バッチング（転写）とシーケンスバッチング（話者分離）を用途別に使い分け

## 使いどころ

- GPU使用率は低いが厳しいレイテンシSLAを求められるリアルタイム音声認識サービス
- 複数の小規模推論ワークロードを1枚のGPUに集約しインフラコストを削減したいチーム
