---
type: guidance
title: GKE Inference Gatewayでモデル別プールへのインテリジェントルーティングを行う推論ネットワーキング
title_original: Networking for AI inference model serving on GKE
industry: cross-industry
cloud:
- gcp
patterns:
- llm-gateway
- guardrails
- inference-optimization
- gpu-fleet-reliability
components:
- GKE Inference Gateway
- Private Service Connect
- Apigee
- Model Armor
- GKE
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/networking-for-ai-inference-gke
published_at: '2026-07-19'
---

## 概要

GKE上でホストする複数モデルのレプリカプールをGKE Inference Gatewayの背後に集約し、プレフィックスマッチングとGPU/TPU負荷に基づくインテリジェントルーティングを行うアーキテクチャ。プロンプト・応答の双方をModel Armorで安全性チェックしてから配信する。

## 設計のポイント

- Inference Gatewayがモデル名でHTTPRouteを解決し、プレフィックスキャッシュと現在の負荷に基づいて最適なレプリカを選ぶ
- 同一モデルの複数レプリカセット（例: 異なるホスティング先のLlama）へトラフィックを比率制御しながら分散する
- リクエスト・レスポンス双方をModel Armorでスクリーニングし、機密情報を含むプロンプトはリダクトまたはブロックする

## 使いどころ

- GKE上に複数の推論サーバーやLoRAアダプタ違いのモデルを多数運用し、一元的なルーティングを行いたいチーム
- GPU/TPUの利用効率を最大化しつつAIガードレールを共通適用したい推論基盤
