---
type: guidance
title: Active DirectoryとGoogle Cloud間のユーザーアカウント自動プロビジョニング(GCDS)
title_original: Active Directory user account provisioning
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: productivity
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-synchronizing-user-accounts
published_at: '2026-07-24'
---

## 概要

本ドキュメントは、Google Cloud Directory Sync (GCDS)を用いてActive DirectoryとCloud IdentityまたはGoogle Workspace間でユーザーおよびグループのプロビジョニングを自動化する手順を解説する。GCDSの配置場所（オンプレミス推奨）、LDAP接続方式、DC Locatorによる複数グローバルカタログサーバーへの対応など、継続的な同期タスクを設定するための設計判断を扱う。
