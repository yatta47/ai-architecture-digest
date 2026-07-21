---
type: guidance
title: Adabas & NaturalをAKSコンテナへリファクタリングするAzure移行アーキテクチャ
title_original: Refactor mainframe computer systems that run Adabas & Natural - Azure Architecture Center
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/refactor-adabas-aks
published_at: '2026-06-12'
---

## 概要

Software AGのAdabas(NoSQLデータベース)とNatural(4GL)で構築されたメインフレームアプリケーションを、AKS上のLinuxコンテナへリファクタリングするアーキテクチャ。ApplinXによる端末エミュレーション、EntireXによるCOBOL/Natural連携、Azure NetApp Filesへの永続データ配置、CONNXによるAdabasデータ仮想化などを組み合わせ、バッチジョブはAdabasと同一ノードに配置して性能劣化を防ぐ。
