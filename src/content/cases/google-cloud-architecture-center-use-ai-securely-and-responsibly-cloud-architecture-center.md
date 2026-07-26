---
type: guidance
title: Secure AI Framework(SAIF)に基づくAIシステムのセキュアな運用原則
title_original: Use AI securely and responsibly
industry: cross-industry
cloud:
- gcp
patterns:
- guardrails
- llmops
- human-in-the-loop
- eval
components:
- Gemini Enterprise Agent Platform
- Vertex Explainable AI
- BigQuery ML
- Cloud Logging
- Knowledge Catalog
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/framework/security/use-ai-securely-and-responsibly
published_at: '2026-07-19'
---

## 概要

Google Cloud Well-Architected FrameworkのセキュリティピラーがGoogleのSecure AI Framework(SAIF)に沿って、AIシステムを安全に使うための原則を整理。データ保護・パイプラインの改ざん耐性・セキュアなデプロイに加え、公平性指標・説明可能性・データリネージ・アカウンタビリティなどAIガバナンス面の実装手段を示す。

## 設計のポイント

- SAIFの6要素に沿って設計初期からデプロイ・運用までホリスティックにAIセキュリティ戦略を組み込む
- Vertex Explainable AIとモデル評価指標(データ/モデルバイアス)を使い、公平性の逸脱を継続的に検知する
- Knowledge CatalogのデータリネージでAI学習データの出所と変換過程を追跡し、バイアスやエラーの原因究明を可能にする
- Cloud LoggingとError Reportingで意思決定の監査証跡を残し、AIシステムのアカウンタビリティを確立する

## 使いどころ

- 生成AIパイプラインを本番導入する前にセキュリティ・プライバシー・コンプライアンス要件を体系的に満たしたい組織
- AIモデルの判断根拠を規制当局や顧客に説明する必要がある金融・医療などの規制業種
- AI活用組織全体でフェアネスやアカウンタビリティのガバナンス体制を立ち上げたいCoE/プラットフォームチーム
