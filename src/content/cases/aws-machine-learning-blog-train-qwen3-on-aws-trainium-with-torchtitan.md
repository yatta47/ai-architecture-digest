---
type: guidance
title: torchtitanでAWS TrainiumにQwen3を学習する3つの方法
title_original: Train Qwen3 on AWS Trainium with torchtitan
industry: cross-industry
cloud:
- aws
patterns:
- fine-tuning
- inference-optimization
components:
- torchtitan
- AWS Trainium
- TorchNeuron
- Hugging Face Transformers
- Qwen3
- Neuron Kernel Interface
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/train-qwen3-on-aws-trainium-with-torchtitan/
published_at: '2026-10-21'
---

## 概要

単一のtrn2.48xlarge上で、torchtitanを使いQwen3を3通りの方法で学習する手順を解説する。Transformers v5をバックエンドに使う方法、torchtitan標準のQwen3に切り替える方法、NKIのMoEカーネルを追加する方法を扱う。いずれも事前学習とファインチューニングに使える。

## 設計のポイント

- TorchNeuronがTrainiumをPyTorchのネイティブデバイスとして登録するため、torchtitanを通常どおり使える。
- config.model_specの切り替えだけでモデル実装を差し替え、同じtorchrun起動形式を保つ。
- オーバーライドの仕組みで独自カーネルを差し込めるようにする。

## 使いどころ

- Trainium上で既存のPyTorch学習コードをほぼそのまま動かしたいチーム。
- 公開モデルを自社データで事前学習またはファインチューニングしたい組織。
