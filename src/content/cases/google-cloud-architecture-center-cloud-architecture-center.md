---
type: guidance
title: 社内開発者プラットフォームのマルチリージョン・マルチテナントアーキテクチャ詳細
title_original: Architecture (enterprise application blueprint)
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
source_url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/architecture
published_at: '2026-07-19'
---

## 概要

本番・非本番・開発の3環境それぞれに複数リージョンのGKEクラスタを配置し、Cloud Service MeshとWorkload Identity Federationでテナントを分離する社内開発者プラットフォームの詳細設計と、その意思決定理由の一覧を示す。
