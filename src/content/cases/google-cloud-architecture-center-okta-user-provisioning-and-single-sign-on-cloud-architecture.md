---
type: guidance
title: OktaによるGoogle Cloudユーザープロビジョニングとシングルサインオン設定
title_original: Okta user provisioning and single sign-on
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
source_url: https://docs.cloud.google.com/architecture/identity/okta-provisioning-and-single-sign-on
published_at: '2026-07-24'
---

## 概要

本ドキュメントは、OktaとCloud IdentityまたはGoogle Workspace間でユーザープロビジョニングとシングルサインオンを構成する手順を解説する。専用の自動化用ユーザーとOUを用意してOktaにスーパー管理者権限を付与し、Okta catalogのGoogle Workspaceアプリケーションを使ってSAML 2.0によるSSOとユーザーの作成・更新・無効化の自動プロビジョニングを有効化する流れを示す。
