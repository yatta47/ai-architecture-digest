---
type: guidance
title: Adabas & NaturalアプリケーションのAzureリホスト(HA構成)
title_original: Rehost Adabas and Natural applications on Azure - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/rehost-adabas-software-ag
published_at: '2026-06-12'
---

## 概要

Software AGのAdabas/Naturalで構築された銀行・保険・行政などの基幹システムを、コード変更なしにAzure VM上へリホストするアーキテクチャ。Application GatewayによるL7負荷分散、複数可用性ゾーンへのVM分散、Redisへのセッション外部化によるNatural Availability Serverの高可用化など、アプリ層とデータ層を分離した構成で可用性とスケーラビリティを確保する。
