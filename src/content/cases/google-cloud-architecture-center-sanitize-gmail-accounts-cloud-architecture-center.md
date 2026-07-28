---
type: guidance
title: Gmailアカウントから企業メールアドレスを取り除く（サニタイズ）手順
title_original: Sanitize Gmail accounts
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
source_url: https://docs.cloud.google.com/architecture/identity/sanitizing-gmail-accounts
published_at: '2026-07-24'
---

## 概要

企業のメールアドレスを代替アドレスとして使っているGmailアカウントから、そのアドレスを意図的に取り除く（サニタイズする）手順を解説する。所有者に管理対象アカウントへの切り替えを促すパターンと、単に企業ドメインとの紐付けだけを強制的に解除するパターンの2通りを扱う。
