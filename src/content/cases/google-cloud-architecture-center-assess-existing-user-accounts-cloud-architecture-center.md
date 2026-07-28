---
type: guidance
title: Google環境に混在する未管理コンシューマーアカウントの洗い出し手法
title_original: Assess existing user accounts
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
source_url: https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts
published_at: '2026-07-24'
---

## 概要

Cloud IdentityやGoogle Workspaceで管理されないコンシューマーアカウントが企業のGoogleサービス利用に混在するリスクを、架空企業Example Organizationの6人の従業員を例に整理したドキュメント。管理対象アカウント、外部IdPと一致するコンシューマーアカウント、一致しないコンシューマーアカウントというパターンごとに、離職者による不正アクセスやMFA未適用などのリスクを説明し、アカウント移行による統合の必要性を示している。
