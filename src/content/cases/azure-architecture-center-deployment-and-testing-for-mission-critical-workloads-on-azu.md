---
type: guidance
title: Azureにおけるミッションクリティカルワークロードのデプロイとゼロダウンタイム更新手法
title_original: Deployment and testing for mission-critical workloads on Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-mission-critical/mission-critical-deploy-test
published_at: '2025-09-22'
---

## 概要

ミッションクリティカルなAzureアーキテクチャでは、インフラと同一のデプロイプロセスでアプリケーションも更新し、既存スタンプに手を加えず新規スタンプへ展開してAzure Front Door経由で徐々にトラフィックを移行するブルーグリーン方式を採用する。GitHubとAzure Pipelinesによるfeature/main/releaseのブランチ戦略で変更を管理し、E2E検証やペネトレーション・カオス・ストレステストを通じてゼロダウンタイムと安全なロールバックを実現する。
