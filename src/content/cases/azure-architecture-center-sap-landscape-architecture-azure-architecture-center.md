---
type: guidance
title: Azure上でのSAPランドスケープ全体設計（ハブ&スポーク・DR構成）
title_original: SAP landscape architecture
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/sap/sap-whole-landscape
published_at: '2026-05-28'
---

## 概要

SAPのハブ・非本番・本番・DR環境を含む企業全体のSAPランドスケープをAzure上にハブ&スポーク型ネットワークで構築するベストプラクティス。ExpressRouteでオンプレミスと接続し、サブスクリプションをリージョナルハブ・非本番・本番に分割してセキュリティと運用の境界を明確にする。
