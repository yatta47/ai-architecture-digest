---
type: guidance
title: デプロイメントスタンプパターンによるマルチテナントスケールアウト
title_original: Deployment Stamps pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/deployment-stamp
published_at: '2026-04-30'
---

## 概要

アプリケーションとデータストアを含む独立した複数のコピー（スタンプ）をテナントの部分集合ごとにデプロイし、ほぼ線形にスケールアウトできるようにするデザインパターン。単一インスタンスのスケール限界やコストの非線形性、テナント分離、更新頻度の異なる顧客への対応などの課題を、スタンプ単位の独立デプロイと地域配置によって解決する。
