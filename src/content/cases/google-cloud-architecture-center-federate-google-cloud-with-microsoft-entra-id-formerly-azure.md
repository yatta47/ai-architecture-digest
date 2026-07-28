---
type: guidance
title: Microsoft Entra IDをIdPとしたGoogle Cloudのフェデレーション設計
title_original: Federate Google Cloud with Microsoft Entra ID (formerly Azure AD)
ai_relevant: false
industry: cross-industry
cloud:
- gcp
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory
published_at: '2026-07-24'
---

## 概要

本ドキュメントは、Microsoft Entra ID(旧Azure AD)をIDプロバイダとして使い、Cloud IdentityまたはGoogle Workspaceとフェデレーションする方法を解説する。Entra IDのテナント・ドメイン・ユーザー・グループの論理構造とGoogle Cloudの組織構造を比較し、単一テナント/複数テナントなどシナリオ別のマッピング方針を整理している。ユーザープロビジョニングとSAMLによるシングルサインオンを組み合わせることで、ID管理をEntra ID側に一元化できる。
