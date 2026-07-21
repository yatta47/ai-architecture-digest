---
type: guidance
title: 多層AKSアプリケーションの単一障害点を潰す4つの高可用性の柱
title_original: High availability for multitier AKS applications - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/aks/aks-high-availability
published_at: '2026-06-13'
---

## 概要

AKS上の多層アプリケーションにおける単一障害点を、冗長性・監視・リカバリ・チェックポイントという4つの高可用性の柱で特定・排除する方法を解説する。クリティカルパス上の各コンポーネントをレプリカ化しロードバランサ配下に置くことに加え、監視されていないレプリカも障害検知が遅れる単一障害点になりうる点を指摘する。
