---
type: guidance
title: オンプレ・マルチクラウドの推論バックエンドを単一エンドポイントに統合するAI推論ネットワーキング
title_original: Networking for AI inference model serving on all backends
industry: cross-industry
cloud:
- gcp
- multi-cloud
patterns:
- llm-gateway
- guardrails
- inference-optimization
components:
- Private Service Connect
- Application Load Balancer
- Service Extensions
- Apigee
- Model Armor
- GKE Inference Gateway
- Cloud Run
- Agent Platform
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/networking-for-ai-inference
published_at: '2026-07-19'
---

## 概要

オンプレ・他クラウド・Google Cloud上に分散したモデルの推論サーバーを、OpenAI API形式のリクエストを受ける単一フロントエンドに統合するリファレンスアーキテクチャ。Service Extensionsでボディベースルーティング・API管理・AIガードレールをロードバランサに差し込む。

## 設計のポイント

- リクエストボディ内のモデル名をヘッダーに書き換えるボディベースルーターで、モデル名だけでバックエンドを振り分ける
- ApigeeでAPI認証・レート制限・クォータ管理を一元化し、Model Armorで送受信プロンプトのガードレールを共通適用する
- モデルのホスト先（Agent Platform／GKE／Cloud Run／オンプレ／他クラウド）を問わず同じフロントエンドから透過的に呼び出せるようにする

## 使いどころ

- 複数プロバイダ・複数ホスティング環境にまたがるモデルを開発者が個別IPを意識せず利用できるようにしたい基盤チーム
- モデル単位でガードレールやAPI管理ポリシーを一元的に適用したいプラットフォームチーム
