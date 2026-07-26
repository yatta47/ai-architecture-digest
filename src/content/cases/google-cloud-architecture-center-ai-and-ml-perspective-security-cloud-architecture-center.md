---
type: guidance
title: AI/MLワークロードのセキュリティ：SAIFに基づく設計原則
title_original: 'AI and ML perspective: Security'
industry: cross-industry
cloud:
- gcp
patterns:
- guardrails
- defense-in-depth
- policy-as-code
components:
- Secure AI Framework (SAIF)
- Security Command Center
- Google Threat Intelligence
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security
published_at: '2026-07-19'
---

## 概要

Google CloudのSecure AI Framework（SAIF）に基づき、ビジネス目標とセキュリティ要件の整合、データの最小化と保護、パイプラインの改ざん耐性、セキュアな実行基盤、入力の検証、出力の監視・応答という一連の原則でAI/MLシステムのセキュリティを設計する方法をまとめている。

## 設計のポイント

- セキュリティ要件を開発の初期段階から定義するshift-leftのアプローチで、後付けの対策コストを避ける
- データ最小化原則に基づき、匿名化・合成データを優先し、PIIの収集自体を抑制する
- データポイズニング・モデル反転・敵対的攻撃など、AI特有の攻撃ベクトルを継続的に監視・評価する体制を組み込む

## 使いどころ

- 規制産業でAI/MLシステムのセキュリティ・コンプライアンス要件を満たす必要がある組織
- 生成AIの入出力に対するガードレールと監査体制を設計したいセキュリティチーム
