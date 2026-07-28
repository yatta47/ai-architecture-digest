---
type: guidance
title: IdP障害時にもGoogle Cloudへのアクセスを維持する事業継続設計
title_original: Best practices for continuous access to Google Cloud
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/security/best-practices-continuous-access-to-google-cloud
published_at: '2026-07-25'
---

## 概要

外部IDプロバイダーの障害時にもGoogle Cloudへのアクセスを維持するための事業継続設計を解説する。緊急アクセスユーザーの作成・冗長化、FIDOセキュリティキーによる保護、バックアップIdPの利用など段階的な対策を示す。
