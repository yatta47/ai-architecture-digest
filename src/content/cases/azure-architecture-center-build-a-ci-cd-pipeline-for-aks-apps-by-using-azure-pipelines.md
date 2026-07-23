---
type: guidance
title: AzureパイプラインによるAKSアプリ向けCI/CD構成
title_original: Build a CI/CD pipeline for AKS apps by using Azure Pipelines
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/aks/aks-cicd-azure-pipelines
published_at: '2025-10-02'
---

## 概要

Azure PipelinesでAKSアプリケーションのCI/CDを構築するリファレンスアーキテクチャ。PRパイプラインでのビルド・テスト・静的解析からCIパイプラインでのコンテナイメージ発行、CDパイプラインによるステージング検証を経て本番AKSへ昇格・デプロイする流れを示す。Azure Monitor管理PrometheusやDefender for Containersによる監視・脆弱性スキャンも組み込まれている。
