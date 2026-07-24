---
type: announcement
title: Unity AI GatewayにAI支出コントロールを追加
title_original: Introducing AI Spend Controls with Unity AI Gateway
company: Databricks
industry: cross-industry
cloud: []
patterns:
- cost-optimization
- llm-gateway
- guardrails
components:
- Unity AI Gateway
- Unity Catalog
- Databricks budgets
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/introducing-ai-spend-controls-unity-ai-gateway
published_at: '2026-07-23'
---

## 概要

Unity AI Gatewayに、ユーザー・ユースケース・ワークスペース・アカウント全体それぞれの粒度で予算アラートを設定できるAI Spend Controlsが追加された。予算超過時にはリクエストを自動停止するハードキャップも設定でき、暴走したリトライループやエージェント実験によるコスト急増を防ぐ。

## 設計のポイント

- ユーザー単位・ユースケース単位・ワークスペース単位・アカウント全体という4つの粒度で予算しきい値を1箇所から設定できる
- アラートだけでなく予算超過時にリクエストを自動停止するハードスペンドキャップを用意し、実損の発生前に止められるようにする
- 全リクエストをUnity Catalogのシステムテーブルにトークン数ではなくDBUコストとして記録し、ユーザー・モデル・プロバイダ・タグ単位で支出を分解できるようにする

## 使いどころ

- 多数のチーム・エージェント・モデルプロバイダが混在する組織でAI支出のガバナンスを一元化したいFinOpsチーム
- コーディングエージェントの暴走リトライなど想定外の高額請求を未然に防ぎたいエンジニアリング組織
