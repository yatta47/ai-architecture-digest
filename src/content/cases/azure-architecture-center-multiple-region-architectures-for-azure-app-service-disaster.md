---
type: guidance
title: Azure App Service を複数リージョンに展開して災害復旧に備える設計手引き
title_original: Multiple-region architectures for Azure App Service disaster recovery
industry: cross-industry
cloud:
- azure
patterns:
- disaster-recovery
- ci-cd
components:
- Azure App Service
- App Service Environment
- Azure Front Door
- Application Insights
- Azure Traffic Manager
- Bicep
- Terraform
- Azure Pipelines
- GitHub Actions
- Azure Storage
data_sources:
- アプリケーション状態
- ファイルシステムコンテンツ
- ヘルスプローブ
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/web-apps/guides/multi-region-app-service/multi-region-app-service
published_at: '2026-07-10'
---

## 概要

App Service は単一リージョン内では可用性が高いが、リージョン全体の障害には耐えられない。本記事は App Service と App Service Environment 向けに、同一構成のアプリを複数リージョンへ独立展開する災害復旧アーキテクチャを、アクティブ/アクティブ・アクティブ/パッシブ・パッシブ/コールドの3方式で整理し、RTO・RPO・コスト・複雑さのトレードオフを比較する。

## 設計のポイント

- RTO/RPO とコストから方式を選び、基幹系はアクティブ/アクティブ、数分許容の高優先度アプリはアクティブ/パッシブ、低優先度はバックアップ&リストアのパッシブ/コールドに割り当てる
- アクティブ/アクティブでは Azure Front Door の広域負荷分散とヘルスプローブ（既定30秒間隔）でフェイルオーバーを自動化し、App Service への直接トラフィックは遮断する
- RPO ゼロを狙うなら CI/CD で両リージョンへ同じビルドを配布する
- アプリ状態はファイルシステムでなく DB や Azure Storage（GZRS/GRS）へ外出しして地理冗長化する

## 使いどころ

- リージョン障害でも継続稼働が必要な Web アプリを Azure 上で運用する場面
- 事業継続計画に沿って RTO/RPO とコストのバランスを取りたいアーキテクト
- 同じく BCP 前提で可用性とコストの両立を担う SRE
