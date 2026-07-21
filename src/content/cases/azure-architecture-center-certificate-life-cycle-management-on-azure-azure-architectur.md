---
type: guidance
title: Azureにおける非統合CA向けTLS証明書ライフサイクル自動管理
title_original: Certificate life cycle management on Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/certificate-lifecycle/
published_at: '2026-06-05'
---

## 概要

DigiCertやGlobalSignのような統合CAと異なり自動更新に対応しない社内・非統合CAの証明書を、Key Vault・Event Grid・Automation・Key Vault拡張機能を組み合わせて自動更新する参照アーキテクチャ。証明書の失効による予期せぬサービス停止を防ぎつつ、タグベースの通知や最小権限の原則を徹底し、Log Analyticsで更新状況を可視化する。
