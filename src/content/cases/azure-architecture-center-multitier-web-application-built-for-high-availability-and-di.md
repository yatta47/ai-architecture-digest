---
type: guidance
title: リージョン間フェイルオーバーに対応した3層WebアプリのHA/DR構成
title_original: Multitier web application built for high availability and disaster recovery
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/infrastructure/multi-tier-app-disaster-recovery
published_at: '2026-06-03'
---

## 概要

Web層・ビジネス層・データ層からなるASP.NET+SQL Serverの3層アプリケーションを、可用性ゾーンとAlways On可用性グループでリージョン内冗長化しつつ、Traffic ManagerとSite Recoveryでセカンダリリージョンへの災害復旧を行う汎用アーキテクチャを解説する。
