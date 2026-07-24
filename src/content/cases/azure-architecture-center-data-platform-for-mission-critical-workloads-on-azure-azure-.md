---
type: guidance
title: ミッションクリティカルワークロード向けAzure Cosmos DBデータ基盤設計
title_original: Data platform for mission-critical workloads on Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-mission-critical/mission-critical-data-platform
published_at: '2025-01-30'
---

## 概要

ミッションクリティカルなワークロードにおいて、状態はコンピュートの外部に極力保持すべきという方針のもと、Azure Cosmos DBのマルチリージョン書き込み・Last Writer Wins競合解決・セッション整合性・カスタムインデックス設計などにより高可用なグローバルデータ基盤を構築する方法を解説する。リージョンスタンプ内ではメッセージブローカーが短期バッファとして機能する。
