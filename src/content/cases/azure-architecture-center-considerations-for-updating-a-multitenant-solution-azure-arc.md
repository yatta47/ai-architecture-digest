---
type: guidance
title: テナントごとに異なる更新要求と自社の運用能力のバランスを取る更新ポリシー設計
title_original: Considerations for updating a multitenant solution
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/updates
published_at: '2025-07-15'
---

## 概要

マルチテナントソリューションの更新ポリシー設計ガイド。テナントごとに更新タイミングへの要求(メンテナンスウィンドウ、規制対応、ロールバック要否)が異なる前提で、提供者側が維持できるバージョン数やゼロダウンタイムデプロイの実現可否とのバランスを取り、更新方針を明確に顧客へ伝達する重要性を説く。
