---
type: guidance
title: AD FSによるActive DirectoryとGoogle Cloudのシングルサインオン連携
title_original: Active Directory single sign-on
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
source_url: https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-configuring-single-sign-on
published_at: '2026-07-24'
---

## 概要

本ドキュメントは、Active Directory Federation Services (AD FS) とSAMLフェデレーションを用いて、Active DirectoryとCloud IdentityまたはGoogle Workspace間でシングルサインオンを構成する手順を解説する。GCDSによるユーザープロビジョニングと組み合わせることで、パスワードなどの認証情報をActive Directory側に一元化し、既存のMFAポリシーをGoogle Cloudへのサインオンにも適用できるようにする。
