---
type: guidance
title: 不要なコンシューマーアカウントを排除（エビクション）する手順
title_original: Evict consumer accounts
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/identity/evicting-consumer-accounts
published_at: '2026-07-24'
---

## 概要

元従業員などが保有する、企業のメールアドレスを使い続けているコンシューマーアカウントについて、意図的に競合アカウントを作成・削除することでアカウント名の変更を強制し、企業ドメインとの紐付けを解除する手順を解説する。信頼されたメールアドレスを悪用したソーシャルエンジニアリングのリスクを軽減する目的がある。
