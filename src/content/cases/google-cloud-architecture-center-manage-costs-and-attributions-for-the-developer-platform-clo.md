---
type: guidance
title: 社内開発者プラットフォームのGKEコスト配賦と最適化の考え方
title_original: Manage costs and attributions for the developer platform
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: cost
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/manage-costs-attributions
published_at: '2026-07-19'
---

## 概要

プロジェクト単位・マルチテナントクラスタ単位・共有コストの3種類に分けてGKE費用を各テナントへ配賦する考え方と、予算アラートやBigQueryエクスポートによる継続的なコスト監視の方法を示す。
