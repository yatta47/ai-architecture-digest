---
type: guidance
title: AzureでMongoDB Atlasにプライベート接続するリファレンス構成
title_original: Deploy MongoDB Atlas in Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/databases/architecture/mongodb-atlas-baseline
published_at: '2025-11-18'
---

## 概要

Azure上のワークロードからMongoDB Atlasクラスターへプライベートエンドポイント経由で安全に接続するための単一リージョン構成とマルチリージョン構成を示すリファレンスアーキテクチャ。MongoDB AtlasはAzure Monitorとネイティブ統合されないため、Azure Functionsで定期的にメトリクスAPIをスクレイピングしApplication Insightsへ可視化する仕組みを併用する。マルチリージョン構成では仮想ネットワークピアリングと複数のプライベートエンドポイントにより、リージョン障害時もアプリケーション変更なしでフェイルオーバーできる。
