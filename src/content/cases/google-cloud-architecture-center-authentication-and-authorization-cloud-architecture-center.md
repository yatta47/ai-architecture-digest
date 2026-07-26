---
type: guidance
title: セキュリティ基盤ブループリント：認証と認可
title_original: Authentication and authorization
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
source_url: https://docs.cloud.google.com/architecture/blueprints/security-foundations/authentication-authorization
published_at: '2026-07-19'
---

## 概要

Cloud Identityを用いた従業員ID管理の方法を解説するセキュリティ基盤ブループリントの一部。既存IdP（Active Directory等）をソースオブトゥルースとしてフェデレーションし、パスワードを同期せずSAML SSOで認証する構成を推奨している。
