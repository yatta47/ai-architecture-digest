---
type: guidance
title: ミッションクリティカルワークロードのヘルスモデリング設計
title_original: Health modeling for mission-critical workloads
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-mission-critical/mission-critical-health-modeling
published_at: '2026-07-10'
---

## 概要

ミッションクリティカルワークロードにおけるヘルスモデリングの設計指針。個々の生の指標ではなく信号機式の統合ステータスでワークロード全体の健全性を可視化するApplication Health Serviceの構成を、Cosmos DB・Event Hubs・Storageに対する並列ヘルスチェックとキャッシュ戦略を交えて解説する。異常時にAzure Front Doorへ迅速に状態を伝搬し、トラフィックを健全なスタンプへ振り向ける仕組みを示している。
