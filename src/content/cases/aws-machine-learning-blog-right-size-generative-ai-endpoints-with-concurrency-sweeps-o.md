---
type: guidance
title: 同時実行数スイープでSageMaker推論エンドポイントを適正サイズ化する
title_original: Right-size generative AI endpoints with concurrency sweeps on Amazon SageMaker AI
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- cost-optimization
components:
- Amazon SageMaker AI
- Amazon SageMaker AI Inference Recommendations
- NVIDIA Nemotron-3 Nano 30B
- vLLM
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/right-size-generative-ai-endpoints-with-concurrency-sweeps-on-amazon-sagemaker-ai/
published_at: '2026-09-22'
---

## 概要

同時リクエスト数を段階的に増やして負荷試験する「concurrency sweep」をAmazon SageMaker AI Inference Recommendationsに組み込み、独自の負荷試験基盤なしにエンドポイントの飽和点とSLA境界を把握できるようにした。スループットとレイテンシの両方を計測し、ピークトラフィックをさばくのに必要なインスタンス数を導出する。

## 設計のポイント

- 同時実行数を64→256→1024と段階的に上げて逐次実行し各水準をクリーンな負荷条件で計測する
- 入出力トークン数やストリーミングの有無を含むワークロードプロファイルを先に定義して現実的なトラフィックを模擬する
- GPUメモリ利用率を0.85に抑えてKVキャッシュの増加余地を確保しプレフィックスキャッシュで再利用性を高める
- スループット最大点・レイテンシSLA超過点・必要インスタンス数の3指標を負荷試験結果から導出する

## 使いどころ

- 生成AIエンドポイントのインスタンス数を勘と手動負荷試験の繰り返しで決めているチーム
- レイテンシSLAを維持しつつGPUコストを最小化したい推論基盤の運用
- RAGや要約のような特定ワークロードパターンに合わせて容量計画を立てたい場合
