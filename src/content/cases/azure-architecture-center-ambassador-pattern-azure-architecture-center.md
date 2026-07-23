---
type: guidance
title: クライアント接続の横断的関心事をサイドカーProxyへ委譲するAmbassadorパターン
title_original: Ambassador pattern
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/ambassador
published_at: '2026-03-19'
---

## 概要

ルーティング・監視・TLS終端・リトライなどのクライアント接続処理を、アプリと同一ホストに配置したAmbassadorプロキシへオフロードする設計パターン。レガシーアプリや複数言語混在環境でも横断機能を統一実装できる。
