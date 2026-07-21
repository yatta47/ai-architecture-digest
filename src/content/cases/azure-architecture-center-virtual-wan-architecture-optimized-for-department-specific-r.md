---
type: case
title: OT/IT混在の製造業ネットワークをAzure Virtual WANで部門別に最適化
title_original: Virtual WAN architecture optimized for department-specific requirements - Azure Architecture Center
ai_relevant: false
industry: manufacturing
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/networking/architecture/performance-security-optimized-vwan
published_at: '2026-06-12'
---

## 概要

OT(運用技術)部門は自社NVA/IDPSによる全量ファイアウォール検査を求め、IT部門は低遅延を優先するという相反する要件を、あるグローバル製造業がAzure Virtual WANハブとカスタムルートテーブルで両立させた実例。セキュリティ最適化環境と性能最適化環境をVNet単位で使い分け、NVA経由/直接ルーティングを切り替えることで、拠点拡大にも柔軟に対応できる設計とした。
