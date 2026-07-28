---
type: guidance
title: コンシューマーアカウントを管理対象アカウントへ移行する手順
title_original: Migrate consumer accounts
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
source_url: https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts
published_at: '2026-07-24'
---

## 概要

個人が作成・管理する既存のコンシューマーアカウントを、本人の同意を得た上でCloud IdentityやGoogle Workspaceの管理対象アカウントへ移行する手順を解説する。未管理・移行済み・競合アカウントといった状態遷移を整理し、ドメイン検証から転送リクエストの送付・承諾までのプロセスを説明する。
