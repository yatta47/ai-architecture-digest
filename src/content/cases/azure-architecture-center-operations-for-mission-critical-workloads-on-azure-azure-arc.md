---
type: guidance
title: ミッションクリティカルなAzureワークロードにおける変更運用の型
title_original: Operations for mission-critical workloads on Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-mission-critical/mission-critical-operations
published_at: '2025-12-05'
---

## 概要

ミッションクリティカルなAzureワークロードでは、アプリケーション・インフラ・設定へのあらゆる変更をCI/CDパイプライン経由で行うことを求めるガイダンス。特にAzure Cosmos DBのAPIキーのような長期利用リソースの認証情報は、ダウンタイムなしでプライマリ/セカンダリキーを切り替えて無停止ローテーションする手順を具体的に示している。
