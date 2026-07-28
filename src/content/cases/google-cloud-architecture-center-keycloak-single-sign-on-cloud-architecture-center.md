---
type: guidance
title: KeycloakをIdPとしたGoogle Cloudシングルサインオン設定
title_original: Keycloak single sign-on
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
source_url: https://docs.cloud.google.com/architecture/identity/keycloak-single-sign-on
published_at: '2026-07-24'
---

## 概要

本ドキュメントは、KeycloakをIdPとしてSAMLフェデレーション経由でCloud IdentityまたはGoogle Workspaceのシングルサインオンを構成する手順を解説する。Cloud Identity側でSAMLプロファイルを作成し、Keycloak側でSAMLクライアントと署名証明書を設定したうえで、組織部門またはグループ単位にSSOプロファイルを割り当てる流れを示す。
