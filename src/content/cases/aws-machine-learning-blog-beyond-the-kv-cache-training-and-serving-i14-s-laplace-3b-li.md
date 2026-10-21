---
type: case
title: AWS Trainium2でi14の線形注意モデルLaplace 3Bを学習・推論
title_original: 'Beyond the KV cache: Training and serving i14''s Laplace 3B linear attention model on AWS Trainium2'
company: i14
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- fine-tuning
components:
- AWS Trainium2
- TorchNeuron Native
- PyTorch
- Gated Linear Attention
- Muon
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/beyond-the-kv-cache-training-and-serving-i14s-laplace-3b-linear-attention-model-on-aws-trainium2-with-native-pytorch/
published_at: '2026-10-20'
---

## 概要

i14のLaplace 3BはGLAによりコンテキスト長に依存せずシーケンス当たり29.5MBの状態を保つ。TorchNeuron NativeでTrainium2に移植し、trn2.48xlarge 1台で約12万トークン/秒の学習、1,280並列で11,544トークン/秒の生成を達成した。

## 設計のポイント

- KVキャッシュの代わりに固定サイズの再帰状態を使い並行数とコストを予測可能にする。
- TritonカーネルをネイティブPyTorch実装に置き換えて独自アーキテクチャを移植する。
- 圧縮による検索品質低下をワークロードごとに評価する。

## 使いどころ

- 長時間動くエージェントや長文書解析を低コストで配信する場面。
