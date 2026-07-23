---
type: guidance
title: Azure Container Appsによるマルチテナント分離モデルの選び方
title_original: Considerations for using Azure Container Apps in a multitenant solution
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/container-apps
published_at: '2026-01-27'
---

## 概要

Azure Architecture Centerは、Azure Container Appsでマルチテナントソリューションを構築する際の分離モデルを整理したガイドを公開した。共有Container Apps、テナント専用Container Apps、テナントごとの専用環境という3つのモデルについて、データ分離・パフォーマンス分離・デプロイ複雑性・運用コストの観点でトレードオフを比較している。信頼できるテナント間の共有環境から、信頼できないテナントを完全分離する専用環境まで、要件に応じた選択指針を示す。
