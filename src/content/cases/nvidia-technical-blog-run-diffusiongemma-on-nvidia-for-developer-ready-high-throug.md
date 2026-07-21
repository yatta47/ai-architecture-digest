---
type: announcement
title: 拡散モデル型LLM「DiffusionGemma」をNVIDIA基盤で高スループット提供
title_original: Run DiffusionGemma on NVIDIA for Developer-Ready, High-Throughput Text Generation
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
- parallel-execution
- llmops
- fine-tuning
components:
- DiffusionGemma
- NVIDIA NIM
- NVIDIA NeMo AutoModel
- NVIDIA Model Optimizer
- NVIDIA H100
- NVIDIA DGX Spark
- NVIDIA DGX Station
- NVIDIA RTX PRO
- Hugging Face
- vLLM
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/run-diffusiongemma-on-nvidia-for-developer-ready-high-throughput-text-generation/
published_at: '2026-06-25'
---

## 概要

Google DeepMindが開発した拡散ベースのLLM「DiffusionGemma」が、NVIDIAのH100・DGX Spark・DGX Station・RTX/RTX PRO上で最適化され、トークンを逐次でなく並列に生成することで高スループットなテキスト生成を実現する。Hugging Face、NVIDIA NIM、NVIDIA NeMo AutoModelを通じてBF16/NVFP4形式で提供され、プロトタイピングから本番デプロイ、ファインチューニングまでDay 0でサポートされる。

## 設計のポイント

- 拡散ベースのデノイジングで1ステップあたり256トークンを並列生成し、逐次デコードのスループット制約を解消する
- Gemma 4 26B A4B MoEアーキテクチャを採用し、総パラメータ25.2Bに対し実効パラメータ3.8Bに抑えることでメモリバウンドな低レイテンシ推論を実現する
- BF16とNVFP4量子化の両チェックポイントを用意し、精度と推論効率のトレードオフを用途に応じて選択できるようにする
- NVIDIA NIMでOpenAI互換APIを持つコンテナ化推論マイクロサービスとして提供し、オンプレミス・クラウド・ハイブリッドへ同一構成でデプロイできるようにする

## 使いどころ

- チャットアシスタントやコパイロット、エージェント型ワークフローなどリアルタイム応答性が求められるアプリケーションの高速化
- DGX SparkやRTXでローカルにプロトタイピングし、DGX StationやH100搭載環境でそのまま本番規模までスケールしたい開発者
- 高並列・低レイテンシなテキスト生成でエンタープライズのサービングコストと同時接続数のバランスを最適化したいAI基盤担当者
- NVIDIA NeMo AutoModelを使いHugging Faceチェックポイントから変換なしでDay 0にドメイン特化のファインチューニングを行いたいチーム
