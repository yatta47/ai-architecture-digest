---
type: case
title: Deepgramの音声認識モデルNova-3をAWS Trainium2へ移植した推論最適化
title_original: How Deepgram optimized voice AI at scale with AWS Trainium
company: Deepgram
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- cost-optimization
- voice-agent
components:
- AWS Trainium2
- Amazon EC2 trn2.3xlarge
- AWS Neuron
- TorchNeuron
- Amazon SageMaker AI
- Nova-3
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-deepgram-optimized-voice-ai-at-scale-with-aws-trainium/
published_at: '2026-10-19'
---

## 概要

DeepgramはAWSのForward Deployed Engineeringと協力し、音声認識モデルNova-3をPyTorchからTrainium2へ移植・チューニングした。1台のtrn2.3xlargeで8レプリカを動かし、オフラインのバッチ処理で従来構成より1ドルあたり11〜70%多くの音声を処理できた。

## 設計のポイント

- TorchNeuronでeager実行によりCPUフォールバックを確認してからtorch.compileへ進み、全演算をアクセラレータ上で動かした。
- エンコーダとデコーダを静的シェイプの別グラフとしてコンパイルし、層ごとの出力一致とWERで精度を検証した。
- データ並列のRustランタイムで自社モデルサーバーからTrainiumを呼び出し、複数レプリカを束ねている。
- スループット重視のバッチ用途に絞ることで、価格性能比の改善を最大化している。

## 使いどころ

- コールセンター分析や医療文字起こしなど大量の音声を安く処理したい場面。
- GPUから専用アクセラレータへ推論基盤を移す際の移植手順を知りたいチーム。
- SageMaker上でモデルを自社VPCにセルフホストしたい顧客。
