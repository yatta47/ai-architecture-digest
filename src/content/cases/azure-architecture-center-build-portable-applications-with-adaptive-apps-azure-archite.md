---
type: guidance
title: アプリの意図と実行環境を分離し、ソブリンクラウドからエッジまで持ち運べる『Adaptive Apps』
title_original: Build portable applications with adaptive apps
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/adaptive-apps
published_at: '2026-08-04'
---

## 概要

データ主権規制や断続接続環境など複数の要因から、同じアプリケーション定義をソブリンクラウド・オンプレミス・エッジなど異なるターゲットに移植できることが調達・運用上の要件になりつつある。Radius・Arc対応Kubernetes・エッジAIパターンを基盤に、開発者はアプリの要求を一度だけ記述し、プラットフォーム運用者が環境ごとのレシピ（サービス・ID・ネットワーク・監視・インフラ）にバインドする『Adaptive Apps』アーキテクチャを提示する。
