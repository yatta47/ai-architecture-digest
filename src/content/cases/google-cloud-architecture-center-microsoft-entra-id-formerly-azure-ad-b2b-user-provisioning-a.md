---
type: guidance
title: Entra ID B2Bゲストユーザー向けプロビジョニングとSSO拡張構成
title_original: Microsoft Entra ID (formerly Azure AD) B2B user provisioning and single sign-on
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
source_url: https://docs.cloud.google.com/architecture/identity/azure-ad-b2b-user-provisioning-and-sso
published_at: '2026-07-24'
---

## 概要

本ドキュメントは、Microsoft Entra ID（旧Azure AD）のユーザープロビジョニングとSSO設定を、Entra B2Bのゲストユーザーにも拡張する手順を解説する。ゲストユーザーのUPNをCloud IdentityまたはGoogle Workspaceのドメインにマッピングし、専用の組織部門(OU)に振り分けたうえで、セッション有効期限を8時間に制限するポリシーを適用することで、招待元テナントでアカウントが削除された後もアクセスが残り続けるリスクを緩和する。
