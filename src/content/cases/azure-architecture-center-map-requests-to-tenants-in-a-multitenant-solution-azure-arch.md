---
type: guidance
title: マルチテナントアプリでリクエストをテナントに紐付ける設計パターン
title_original: Map requests to tenants in a multitenant solution
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/map-requests
published_at: '2026-01-21'
---

## 概要

マルチテナントアプリケーションで受信リクエストを正しいテナントに紐付けるための設計ガイド。テナント専用ドメイン名、URLパスやクエリ文字列・カスタムHTTPヘッダーといったリクエストプロパティ、OAuth 2.0やSAMLのトークンクレーム、APIキーという複数の識別アプローチを挙げ、それぞれの利便性・セキュリティ・運用上のトレードオフを整理している。
