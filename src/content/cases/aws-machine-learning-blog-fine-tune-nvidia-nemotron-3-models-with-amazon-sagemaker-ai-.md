---
type: announcement
title: Amazon SageMaker AIのサーバーレスモデルカスタマイズでNVIDIA Nemotron 3をファインチューニング
title_original: Fine-tune NVIDIA Nemotron 3 models with Amazon SageMaker AI serverless model customization
industry: cross-industry
cloud:
- aws
patterns:
- fine-tuning
- reinforcement-learning
- llmops
components:
- Amazon SageMaker AI
- NVIDIA Nemotron 3 Nano
- NVIDIA Nemotron 3 Super
- SageMaker Studio
- NeMo Gym
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/fine-tune-nvidia-nemotron-3-models-with-amazon-sagemaker-ai-serverless-model-customization/
published_at: '2026-07-10'
---

## 概要

Amazon SageMaker AIは、Mamba-TransformerハイブリッドMoEアーキテクチャを持つNVIDIA Nemotron 3（Nano 30B/Super 120B）向けにサーバーレスモデルカスタマイズを提供開始し、GPUクラスタの構築・運用なしにSFT・RLVR・RLAIFによるファインチューニングが可能になった。企業は自社のドメイン語彙やツール呼び出し、ブランドボイスに合わせてオープンウェイトモデルを特化させつつ、機密データを自社インフラ内に留めコストを抑えられる。

## 設計のポイント

- サーバーレスでGPUクラスタのプロビジョニング・分散学習構成・チェックポイント管理を不要にし、データとユースケースの検討に集中できるようにする。
- タスク特性に応じてSFT（模範データによる教師あり学習）・RLVR（検証可能な報酬によるRL）・RLAIF（AIフィードバックによるRL）を使い分ける。
- Mamba-2層・Transformer注意層・Latent MoE層を組み合わせたハイブリッドアーキテクチャで、パラメータの一部のみ活性化させ高スループット・低コストを両立する。
- 小型モデル(Nano)を特定タスクに特化ファインチューニングすることで、大型モデル相当の性能をより低コストで達成する。

## 使いどころ

- 独自のツール呼び出しAPIやブランドボイス、業界特有の意思決定パターンに合わせてオープンウェイトLLMを適応させたい企業。
- コーディング支援・ITチケット自動化・サイバーセキュリティトリアージなど、持続的な多段階推論を要するマルチエージェントアプリケーションを構築するチーム。
