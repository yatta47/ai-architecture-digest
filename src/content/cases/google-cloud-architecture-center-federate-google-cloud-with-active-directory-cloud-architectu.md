---
type: guidance
title: Active DirectoryとGoogle Cloudのフェデレーション設計
title_original: Federate Google Cloud with Active Directory
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
source_url: https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction
published_at: '2026-07-24'
---

## 概要

Active DirectoryをIdPかつ真正情報源としてCloud IdentityやGoogle Workspaceと連携させる方法を解説する記事。Google Cloud Directory Sync（GCDS）によるユーザー・グループのプロビジョニングと、AD FSによるSAMLベースのシングルサインオンという2つの要素、およびフォレストやドメインをGoogle Cloud組織へどうマッピングするかを詳しく説明している。
