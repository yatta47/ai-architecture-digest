---
type: guidance
title: ストラングラーフィグパターン：レガシーシステムの段階的移行
title_original: Strangler Fig pattern
ai_relevant: false
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig
published_at: '2026-06-02'
---

## 概要

ファサードでリクエストを新旧システムに振り分けながら、機能を少しずつ新システムへ移行していく段階的モダナイゼーションパターン。クライアントに移行を意識させずに、最終的にレガシーシステムを廃止できる。
