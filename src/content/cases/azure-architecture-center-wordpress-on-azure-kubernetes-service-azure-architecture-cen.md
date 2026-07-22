---
type: guidance
title: 大規模WordPressをAKS＋Azure NetApp Filesでホストする構成
title_original: WordPress on Azure Kubernetes Service
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/infrastructure/wordpress-container
published_at: '2026-06-03'
---

## 概要

ストレージ負荷の大きい大規模WordPressサイトを、AKS・Azure Front Door・Azure NetApp Files・Managed Redisで構成するコンテナ基盤。Front DoorのPrivate Link経由アクセスとポッドオートスケーリングで可用性とパフォーマンスを両立する。
