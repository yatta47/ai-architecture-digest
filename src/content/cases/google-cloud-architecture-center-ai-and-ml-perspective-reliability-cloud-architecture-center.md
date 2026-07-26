---
type: guidance
title: AI/MLシステムの信頼性設計：スケーラブルな推論基盤とMLOps
title_original: 'AI and ML perspective: Reliability'
industry: cross-industry
cloud:
- gcp
patterns:
- gpu-fleet-reliability
- disaster-recovery
- rag
components:
- Vertex AI
- GKE
- Dataflow
- vLLM
- Ollama
- Cloud Run
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/reliability
published_at: '2026-07-19'
---

## 概要

SRE原則に基づき、AI/MLワークロードのスケーラブルで高可用な推論基盤、疎結合なMLOpsパイプライン、データ・モデルガバナンス、包括的なオブザーバビリティを設計する原則をまとめている。GPUのXidエラー監視・複数リージョンへのモデル配信・RAG用ベクトルDBの高可用化などAI特有の信頼性課題に言及する。

## 設計のポイント

- オンライン推論エンドポイントは最低2レプリカ・複数リージョンで構成し、トラフィックに応じたオートスケールを組み込む
- GPUのXidエラーを監視し、リセットやホスト交換などの復旧アクションを自動化してGPUフリート全体の信頼性を担保する
- RAG用のベクトルデータベースを含む重要コンポーネントに、マルチゾーン/マルチリージョンの冗長性を持たせる

## 使いどころ

- 本番のリアルタイム推論やRAGシステムで高可用性が求められるプロダクト
- GPU/TPUクラスタの障害を前提にした大規模学習・推論基盤を運用するチーム
