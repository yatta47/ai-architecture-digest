---
type: guidance
title: アカウント統合とフェデレーションを両立させる移行時の設定パターン
title_original: Assess the impact of user account consolidation on federation
ai_relevant: false
industry: cross-industry
cloud:
- gcp
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/identity/assessing-consolidation-impact-on-federation
published_at: '2026-07-24'
---

## 概要

外部IdPとのフェデレーションを維持しながら既存のコンシューマーアカウントを段階的に統合する際に生じるコンフリクティングアカウントや意図しない削除のリスクを解説し、それを回避するための一時的な設定要件をまとめたドキュメント。Microsoft Entra IDとの連携を例に、プロビジョニングを構成しない、または一致しないアカウントの削除を防ぐなど複数のアプローチとそのトレードオフを示している。
