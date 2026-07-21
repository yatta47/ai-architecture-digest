---
type: guidance
title: Azure Virtual Desktop上でのEsri ArcGIS Pro GISプラットフォーム構成
title_original: Deploy Esri ArcGIS Pro in Azure Virtual Desktop
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/data/esri-arcgis-azure-virtual-desktop
published_at: '2026-06-11'
---

## 概要

Esri ArcGIS ProをAzure Virtual Desktop上にデプロイし、GPUを活用した2D/3Dの地理空間ワークフローをリモートデスクトップ経由で提供するリファレンスアーキテクチャ。ArcGIS Enterprise（Server、Data Store、Portal）をバックエンドに、Azure NetApp Filesで構成データやラスタ・LiDARデータを高速配信し、Azure SQL Managed Instanceでエンタープライズジオデータベースを管理する。GISアナリストや管理者は低遅延のRDPセッションからArcGIS Proを利用し、外部公開が必要な場合はApplication Gateway経由でWeb GISにアクセスする。
