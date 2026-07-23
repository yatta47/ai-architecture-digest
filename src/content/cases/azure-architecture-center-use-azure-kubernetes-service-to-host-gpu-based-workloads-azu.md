---
type: guidance
title: AKSでGPUワークロードをホストするリファレンスアーキテクチャ
title_original: Use Azure Kubernetes Service to host GPU-based workloads
industry: cross-industry
cloud:
- azure
patterns:
- inference-optimization
- gpu-fleet-reliability
- cost-optimization
components:
- Azure Kubernetes Service
- TensorFlow
- PyTorch
- vLLM
- Triton Inference Server
- Azure Machine Learning
- NVIDIA CUDA
- NVIDIA cuDNN
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-gpu/gpu-aks
published_at: '2026-01-07'
---

## 概要

AKS上でGPUノードを効率的にホストするためのリファレンスアーキテクチャで、データサイエンス、機械学習/深層学習、コンピュータビジョン、動画処理、HPC、ゲノム解析、そして生成AI（LLMの学習・推論）まで、GPUが有効な代表的ワークロードを整理する。TensorFlow・PyTorch・vLLM・Triton Inference Serverなどのフレームワーク選定やAzure Machine Learningのマネージドオンラインエンドポイントによる推論配信、GPUノードプールのベストプラクティスを示し、GPUが不要なワークロードを見極めてコストを抑える判断軸も提供する。NBAやAI企業Mr. Turingの事例にも触れている。

## 設計のポイント

- ワークロード特性（スループット重視の並列計算か、複雑な分岐ロジックか）に応じてGPUノードプールを使うかCPUのままにするかを判断する
- LLMや生成AIモデルの推論はTriton Inference ServerやvLLMなど専用の推論サーバーを使い、Azure Machine Learningのマネージドオンラインエンドポイントで提供する
- GPUベンダー（NVIDIA/AMD）のKubernetesデバイスプラグインを導入し、用途に応じたVM SKU選定を先に固めてからノードプールを設計する
- 生成AIモデル（GPT/Llama/Phi等）の学習・推論の両方でGPUの並列処理を活用し、チャットボットやAIアシスタントのレイテンシを下げる

## 使いどころ

- データサイエンス・コンピュータビジョン・動画処理・HPC・ゲノム解析など計算集約型ワークロードをAKSでスケールさせたいチーム
- LLMや生成AIモデルのオンライン推論をAKS上でスケーラブルに配信したい場合
- GPUコストを抑えるため、GPUが本当に必要なワークロードのみを見極めたいアーキテクトやプラットフォームチーム
