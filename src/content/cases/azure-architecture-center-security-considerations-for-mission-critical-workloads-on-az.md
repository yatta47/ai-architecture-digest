---
type: guidance
title: AKSベースのミッションクリティカルワークロードにおけるセキュリティ設計指針
title_original: Security considerations for mission-critical workloads
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-mission-critical/mission-critical-security
published_at: '2025-09-22'
---

## 概要

ミッションクリティカルなワークロードでは可用性と信頼性を守るためにセキュリティ対策が不可欠であるとし、AKSを中心とした構成における最小権限アクセス、マネージドIDの利用、Key Vaultによるシークレット管理、カスタムドメインとTLS証明書の自動更新などの実践を解説する。開発者は本番インフラに直接アクセスせず、デプロイパイプラインやCSIドライバー経由でシークレットや証明書を安全かつ自動的に扱う設計が示されている。
