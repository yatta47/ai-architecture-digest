---
type: guidance
title: マルチテナントソリューションにおけるAzure NAT GatewayでのSNATポート枯渇対策
title_original: How to use Azure NAT Gateway in a multitenant solution
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/nat-gateway
published_at: '2026-05-26'
---

## 概要

マルチテナントアプリケーションで発生しがちなSNATポート枯渇問題を、Azure NAT Gatewayの動的ポート割り当てとスケールアウトで緩和する方法を解説する記事。テナントごとに固定送信元IPを分離する隔離モデルの選び方も示す。
