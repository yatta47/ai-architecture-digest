---
type: guidance
title: Azure Update Managerで大規模Windows VM群のパッチ適用を統制する
title_original: Scalable Windows virtual machine patch management
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/virtual-machines/patch-management
published_at: '2026-07-28'
---

## 概要

Azure上のWindows VM群に対するOSアップデートを、Azure Update Managerを用いて一貫性のあるガバナンス付きで運用する方法を解説するアーキテクチャガイド。メンテナンス構成をリージョン・サブスクリプション単位のIaCリソースとして管理し、Azure Policyで設定ドリフトを自動是正する構成を推奨する。
