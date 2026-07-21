---
type: guidance
title: Microsoft Fabricで作るグリーンフィールド・レイクハウス基盤
title_original: Greenfield lakehouse on Microsoft Fabric
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/data/greenfield-lakehouse-fabric
published_at: '2026-06-11'
---

## 概要

Microsoft Fabricを使ってゼロからスケーラブルなデータプラットフォームを構築するリファレンスアーキテクチャ。バッチ処理はメダリオンアーキテクチャ（ブロンズ/シルバー/ゴールド）でDelta Lakeとマネージドの Spark ランタイムを用い、リアルタイム処理はFabric Real-Time Intelligenceのイベントストリームで低遅延の分析を実現するLambdaアーキテクチャを採用する。OneLakeとMicrosoft Purviewを基盤サービスとし、Power BIやSQLエンドポイントなど多様な消費層へデータを提供する。
