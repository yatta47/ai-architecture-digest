---
type: announcement
title: SageMaker AIリアルタイムエンドポイントがKVキャッシュ認識ルーティングに対応
title_original: Amazon SageMaker AI real-time endpoints now support KV cache aware routing
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
components:
- Amazon SageMaker AI
- KV cache
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-real-time-endpoints-now-support-kv-cache-aware-routing/
published_at: '2026-11-17'
---

## 概要

SageMakerのリアルタイムエンドポイントに、モデルコンテナが報告するキャッシュ状態を用いるKV-awareルーティングが追加された。長い共通プロンプトを持つリクエストを、既に長い一致キャッシュを保持し過負荷でないインスタンスへ送る。環境変数1つとRoutingStrategy=KV_AWAREで有効化できる。

## 設計のポイント

- リクエストのハッシュ推定ではなく、実際のキャッシュ内容の報告に基づいて経路を決める。
- キャッシュ一致と負荷のバランスを考慮する。
- クライアントAPIは変更せずに有効化できる。

## 使いどころ

- マルチターン会話や長いシステムプロンプトを持つLLM提供。
- RAGやエージェントで共通プレフィックスが多いワークロード。
