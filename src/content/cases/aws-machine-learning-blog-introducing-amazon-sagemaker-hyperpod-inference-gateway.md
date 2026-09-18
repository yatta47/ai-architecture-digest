---
type: announcement
title: SageMaker HyperPod Inference GatewayによるGPU認識型LLMルーティング
title_original: Introducing Amazon SageMaker HyperPod Inference Gateway
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- llm-gateway
- multi-model-routing
components:
- Amazon SageMaker HyperPod Inference Gateway
- Amazon EKS
- Envoy Gateway
- Prometheus
- Amazon CloudWatch
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-inference-gateway/
published_at: '2026-09-18'
---

## 概要

Kubernetesのラウンドロビン/最小接続ルーティングはGPU内部のKVキャッシュ使用率やLoRAアダプタの常駐状況を考慮できず、初回トークンのレイテンシ悪化とGPUの過剰プロビジョニングを招いていた。SageMaker HyperPod Inference Gatewayは、EKSマネージドアドオンとしてリアルタイムGPUシグナルに基づくルーティングを提供し、アプリケーション側の変更なしに初回トークンレイテンシを最大82%削減する。

## 設計のポイント

- KVキャッシュ使用率・キュー深さ・LoRAアダプタ常駐・プレフィックスキャッシュヒット率・実行中リクエスト数を重み付けしたスコアリングで最適なpodへリクエストを振り分ける
- Body-Based Routerがリクエストボディのmodelフィールドを見て複数モデルを1つのゲートウェイに集約し、アプリ側のルーティングロジックを不要にする
- OpenAI互換のエンドポイントを維持することでクライアントコード変更ゼロで導入でき、pod障害時は健全なpodへ自動フェイルオーバーする段階的な縮退設計を持つ

## 使いどころ

- 同一GPUクラスタ上で複数のLLMやLoRAアダプタを共有運用し、GPUの無駄遣いを減らしたいプラットフォームチーム
- バースト時の初回トークンレイテンシのばらつきを抑えたいチャットボット等のレイテンシ敏感なサービス
- 既存のKubernetes/EKS基盤に手を入れずにGPU認識ルーティングを追加導入したいチーム
