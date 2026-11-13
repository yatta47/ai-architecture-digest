---
type: announcement
title: AWS TrainiumでSGLangを動かすSGLang-Neuron
title_original: Deploy frontier AI models on AWS Trainium with SGLang-Neuron
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
components:
- SGLang-Neuron
- AWS Trainium
- TorchNeuron
- Neuron Kernel Interface
- NIXL
- Elastic Fabric Adapter
- Amazon EC2
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/deploy-frontier-ai-models-on-aws-trainium-with-sglang-neuron/
published_at: '2026-11-12'
---

## 概要

SGLang-NeuronがAWS Deep Learning Containerとして一般提供され、既存のSGLangのインターフェースのままTrainium上でモデル配信とRLロールアウトができる。アウトオブツリーのプラグインで、PD分離にも対応する。

## 設計のポイント

- アウトオブツリープラグインにより、Trainium対応とSGLang本体を独立して進化させる。
- 標準PyTorchとNKIカーネルをtorch.compileで統合して実行する。
- PD分離ではprefillからdecodeへKVキャッシュをEFA経由で転送する。

## 使いどころ

- GPU以外のアクセラレータでLLM配信コストを下げたいチーム。
- RLロールアウト生成と推論を同じ基盤で回したい組織。
