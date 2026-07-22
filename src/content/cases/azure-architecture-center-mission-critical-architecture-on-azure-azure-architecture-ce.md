---
type: guidance
title: Azure上でミッションクリティカルなワークロードを設計するためのリファレンスアーキテクチャ
title_original: Mission-critical architecture on Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-mission-critical/mission-critical-intro
published_at: '2026-04-03'
---

## 概要

本記事は、可用性99.99%以上を目標とするミッションクリティカルなワークロードをAzure上で設計するための指針をまとめたリファレンスアーキテクチャである。マルチリージョンのアクティブ・アクティブ構成、可用性ゾーン活用、デプロイメントスタンプ、IaCによる再現可能なブルー/グリーンデプロイ、フェデレーテッドな監視と階層的ヘルスモデルなど、信頼性を高めるための設計戦略を提示している。
