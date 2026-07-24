---
type: guidance
title: 自前の認証基盤を作らずIDaaSを採用すべき理由
title_original: Use an Identity as a Service platform
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/identity
published_at: '2025-02-05'
---

## 概要

クラウドアプリのID管理は自前構築ではなくMicrosoft Entra IDのようなIDaaS（Identity as a Service）に任せるべきだと説く記事。認証情報の保管リスク、OAuth 2/OpenID Connectなどプロトコルの複雑さ、パスワードレス認証・SSO・MFA・条件付きアクセスといった高度機能、SLAに基づく可用性・性能をIDaaSに委譲するメリットを整理している。
