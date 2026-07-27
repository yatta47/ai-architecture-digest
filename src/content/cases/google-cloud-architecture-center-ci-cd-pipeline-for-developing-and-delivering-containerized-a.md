---
type: guidance
title: Cloud Code/Build/Deployで作るコンテナアプリ向けCI/CDパイプライン
title_original: CI/CD pipeline for developing and delivering containerized apps
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: speed
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke
published_at: '2026-07-19'
---

## 概要

Cloud Code・Cloud Build・Cloud Deployを組み合わせ、GKEへのコンテナアプリ開発からステージング・本番デプロイまでを一貫させるリファレンスアーキテクチャ。Skaffoldで開発/ステージング/本番の設定を共通化し、本番反映は手動承認を挟む。
