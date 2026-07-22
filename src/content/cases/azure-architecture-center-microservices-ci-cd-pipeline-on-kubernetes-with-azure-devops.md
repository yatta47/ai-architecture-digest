---
type: guidance
title: Helm×Azure DevOpsによるAKSマイクロサービスCI/CDパイプライン
title_original: Build a CI/CD pipeline for microservices on Kubernetes with Azure DevOps and Helm
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/microservices/ci-cd-kubernetes
published_at: '2026-05-29'
---

## 概要

モノレポ・トランクベース開発・リリースブランチを前提に、Azure PipelinesでビルドしHelmチャートをACRへプッシュ、QA環境を経て承認後に本番AKSへデプロイするCI/CDパイプラインの設計例。チーム独立デプロイと環境分離の実践を示す。
