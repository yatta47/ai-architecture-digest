---
type: guidance
title: 米連邦政府向けGemini導入におけるコンプライアンス設計
title_original: Deployment guidance for Gemini for Government
industry: public-sector
cloud:
- gcp
patterns:
- ai-agent
- llmops
- policy-as-code
- defense-in-depth
components:
- Gemini Enterprise
- Vertex AI
- Model Armor
- Assured Workloads
- BigQuery
- Looker
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/security/deploy-gemini-gov
published_at: '2026-07-25'
---

## 概要

米連邦機関・国防総省がFedRAMP High/DoD IL4要件下でGemini for Governmentを導入するための技術ガイド。Assured Workloads境界内へのリソース配置と、機能ごとの認可状況に応じたアクセス制御を規定する。

## 設計のポイント

- Assured Workloadsフォルダ配下にリソースを配置し、コンプライアンス体制(FedRAMP High/IL4)ごとに境界を明確化する
- 機能ごとにFedRAMP High・IL4の認可状況が異なるため、サービス/機能単位で許可リストを管理する
- グローバルエンドポイントのみのモデルはデータレジデンシーに非対応のため、組織ポリシーでアクセスを制限する
- 未認可機能(画像生成やパーソナライズ記憶など)は手動で無効化し、無効化できない機能は運用者教育でリスクを緩和する

## 使いどころ

- FedRAMP High/DoD IL4準拠が求められる米連邦・国防機関での生成AIエージェント導入
- 規制の厳しい環境でAIサービスの認可境界とデータレジデンシーを設計するクラウドアーキテクト
