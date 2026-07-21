---
type: guidance
title: 外部IDプロバイダーに認証を委譲するFederated Identityパターン
title_original: Federated Identity pattern
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/federated-identity
published_at: '2026-07-02'
---

## 概要

複数のパートナー企業が提供するアプリケーションごとに異なるログイン情報を管理する負担を解消するため、認証を信頼できる外部IDプロバイダー（IdP）とセキュリティトークンサービス（STS）に委譲する「Federated Identityパターン」を解説する。アプリケーションはクレームベースのトークンを受け取って認可判断を行うだけでよく、パスワード管理やアカウント失効などID管理の責務をIdP側に集約できる。エンタープライズSSOや複数パートナーとのB2B連携など、認証基盤を自前で持たずに標準化したい場面に適したデザインパターンとして紹介されている。
