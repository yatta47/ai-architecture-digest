---
type: guidance
title: Terraform/SkaffoldによるApache Guacamole on GKEの構築手順
title_original: Deploy Apache Guacamole on GKE and Cloud SQL
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
source_url: https://docs.cloud.google.com/architecture/deploy-guacamole-gke/deployment
published_at: '2026-07-19'
---

## 概要

前掲のGuacamole on GKEアーキテクチャをTerraformでインフラ構築し、Cloud SQLにデータベースを作成、SkaffoldでGKEクラスタへアプリをデプロイしてIAP経由の接続を検証する手順ガイド。
