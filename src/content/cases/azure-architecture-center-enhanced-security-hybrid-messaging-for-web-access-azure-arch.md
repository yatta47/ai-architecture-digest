---
type: guidance
title: Exchange Online/オンプレミスの多要素認証によるハイブリッドメッセージングWebアクセス保護
title_original: Enhanced-security hybrid messaging infrastructure for web access
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/hybrid/secure-hybrid-messaging-web
published_at: '2026-06-03'
---

## 概要

Exchange OnlineとExchangeオンプレミスの両方でOutlook on the webへのアクセスを保護するアーキテクチャ。Microsoft Entra ID、Conditional Access、AD FSと連携し、Webアクセス時に多要素認証(MFA)を必須化することで従来型認証からの移行を実現する。フェデレーションID・パススルー認証などハイブリッドID構成の違いを踏まえた認証フロー設計を示す。
