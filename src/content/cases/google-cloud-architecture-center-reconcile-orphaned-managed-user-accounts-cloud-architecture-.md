---
type: guidance
title: 外部IdPと同期しない孤立した管理対象ユーザーアカウントの解消手順
title_original: Reconcile orphaned managed user accounts
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
source_url: https://docs.cloud.google.com/architecture/identity/reconciling-orphaned-managed-user-accounts
published_at: '2026-07-25'
---

## 概要

外部IDプロバイダーを正とする環境で、Cloud IdentityやGoogle Workspace側にのみ存在し外部ソースに対応するIDを持たない『孤立アカウント』を検出・解消する手順を解説する。Active DirectoryやMicrosoft Entra IDとのアカウント突合方法や、削除・保留・主メールアドレス修正といった解消パターンを示す。
