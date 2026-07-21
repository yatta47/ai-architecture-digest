---
type: guidance
title: App Service Environmentで構築するセキュアなWebアプリケーション基盤（経費精算システム例）
title_original: Securely managed web applications
ai_relevant: false
industry: financial-services
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/apps/fully-managed-secure-apps
published_at: '2026-07-02'
---

## 概要

App Service Environmentを中核に、Application GatewayとWeb Application Firewallでインターネットからのアクセスを制御し、Azure DevOpsによるCI/CDを統合したセキュアなWebアプリケーション構成を、経費精算システムを例に解説する。オンプレミスからのExpressRoute/VPN接続、内部ロードバランサー経由のトラフィック制御、SQL Databaseへのサービスエンドポイント接続などにより、プラットフォームとアプリケーション両レベルでのセキュリティを重視する銀行・保険業界などでの採用を想定している。
