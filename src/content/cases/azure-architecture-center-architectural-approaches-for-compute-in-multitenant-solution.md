---
type: guidance
title: マルチテナントソリューションにおけるコンピューティング層の設計指針
title_original: Architectural approaches for compute in multitenant solutions
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/compute
published_at: '2026-06-23'
---

## 概要

Azure Architecture Centerによる、マルチテナントソリューションのコンピューティング層を設計する際の主要な考慮事項をまとめたガイダンス記事。スケーリング方針（水平/垂直スケール、テナント数に応じたスケールトリガー）、ステート管理（ステートレス化、セッションアフィニティ、外部キャッシュの活用）、テナント分離モデル（共有・専有・準分離）の選び方を整理している。ノイジーネイバー問題の回避やAzure Chaos Studioによる障害注入テストなど、信頼性確保のための実践的な指針も示されている。
