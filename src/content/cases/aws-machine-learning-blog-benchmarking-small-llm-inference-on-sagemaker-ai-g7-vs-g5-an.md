---
type: guidance
title: SageMaker AIでのG7/G5/G6 GPU比較によるLLM推論コスト最適化
title_original: 'Benchmarking small LLM inference on SageMaker AI: G7 vs G5 and G6'
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
components:
- Amazon SageMaker AI
- NVIDIA Blackwell
- Qwen3-Coder-30B
- NVIDIA Nemotron-3-Nano
- vLLM
- DJL LMI
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/benchmarking-small-llm-inference-on-sagemaker-ai-g7-vs-g5-and-g6/
published_at: '2026-09-08'
---

## 概要

SageMaker AIのGenerative AI推論レコメンデーション機能を使い、30BのMoEモデル2種をG5・G6・G6e・G7の各GPUインスタンスでベンチマークする。Blackrock世代のG7はネイティブFP4 Tensor Core対応により、GPU数が半分でもレイテンシ・スループット・コスト効率で優位という結果を示す。

## 設計のポイント

- MoEモデルはデコード時にメモリ帯域律速なため、GPU世代間のメモリ帯域差がそのまま性能差になる
- G7のみがネイティブFP4 Tensor Coreに対応し、NVFP4量子化でモデルサイズと精度劣化のトレードオフを改善する
- 既存エンドポイントの直接ベンチマークと、要件から構成を自動提案するレコメンデーションの2workflowを使い分ける

## 使いどころ

- コーディングアシスタント等のLLM推論でGPUインスタンス選定のコスト対性能を最適化したい場合
- MoEモデルを本番投入する前に複数世代のGPUを定量比較したいチーム
