---
type: announcement
title: プレフィックス共有リクエストを同一インスタンスへ寄せてKVキャッシュ効率を高めるルーティング
title_original: Reduce LLM latency with prefix-aware routing on Amazon SageMaker Inference
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
components:
- Amazon SageMaker Inference
- vLLM
- TensorRT-LLM
- Llama 3.1 70B
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/reduce-llm-latency-with-prefix-aware-routing-on-amazon-sagemaker-inference/
published_at: '2026-09-10'
---

## 概要

Amazon SageMaker Inferenceに、同じプロンプトの先頭(プレフィックス)を持つリクエストを同一インスタンスへ送るPREFIX_AWAREルーティング戦略が追加された。Llama 3.1 70Bでのベンチマークでは、フリート全体のKVキャッシュヒット率が約25%から80%超に上がり、P50 TTFTが最大77%削減、スループットも最大16%向上した。

## 設計のポイント

- プロンプトの先頭(プレフィックス)を見て同じ内容を同じインスタンスに送ることで、フリート全体でのKVキャッシュヒット率を引き上げる
- 過負荷時は自動的に別インスタンスへフォールバックし、キャッシュ効率と負荷分散のバランスを取る
- スケールイン/アウト時もほとんどのリクエストの割り当て先を維持し、キャッシュの無効化を避ける

## 使いどころ

- RAGで同じドキュメントを複数ユーザーが参照するワークロード
- 長い会話履歴を毎ターン送るマルチターン対話アプリ
- 長大なシステムプロンプト/指示文を持つテンプレート型ボット
