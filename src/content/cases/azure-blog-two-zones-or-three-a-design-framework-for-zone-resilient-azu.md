---
type: guidance
title: ゾーン数はコンポーネント単位で決める、Azureのゾーン耐障害設計フレームワーク
title_original: Two zones or three? A design framework for zone-resilient Azure workloads
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/two-zones-or-three-a-design-framework-for-zone-resilient-azure-workloads/
published_at: '2026-09-09'
---

## 概要

Microsoftは、Azureワークロードのゾーン耐障害設計において『何ゾーン必要か』をワークロード全体ではなくコンポーネント単位で判断するフレームワークを提示する。ステートレスな層は2ゾーンで十分な場合が多い一方、クォーラムや合意形成を伴うステートフルなコンポーネントは3ゾーン目の障害ドメインを必要とすることが多いとする。
