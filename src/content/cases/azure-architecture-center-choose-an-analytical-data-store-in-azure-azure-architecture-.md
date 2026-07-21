---
type: guidance
title: Lambdaアーキテクチャのサービングレイヤーに適した分析データストアをFabric/Databricks/Cosmos DBから選ぶ
title_original: Choose an analytical data store in Azure
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/analytical-data-stores
published_at: '2026-06-18'
---

## 概要

ビッグデータアーキテクチャのサービングレイヤー（ホットパス・コールドパスの両方をクエリ対象にする層）に適した分析データストアを、Microsoft Fabric各種（Lakehouse、Data Warehouse、Eventhouse、SQL Database）、Azure Databricks、Azure SQL Database、Azure Cosmos DBなどから選ぶための基準を整理する。キーバリュー・ドキュメント・列指向・グラフ・時系列といったデータモデルごとの向き不向きと、速度優先のサービングレイヤーかどうかといった選定基準を、機能比較表とともに提示している。
