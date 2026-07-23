---
type: guidance
title: Azureにおけるデータストアモデルの選定ガイド
title_original: Understand data models
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/understand-data-store-models
published_at: '2025-09-23'
---

## 概要

現代のシステムは取引、イベント、ドキュメント、テレメトリなど多様なデータを扱うため、単一のデータストアでは全てのアクセスパターンを効率的に満たせないとし、複数のストレージモデルを併用するポリグロットパーシステンスを推奨している。リレーショナル、ドキュメント、キーバリュー、列指向、グラフ、時系列、オブジェクト/ファイル、検索・インデックス、ベクトル、分析(OLAP/MPP)という主要なデータモデルを整理し、それぞれの特徴・典型的ワークロード・代表的なAzureサービスを比較表で示す。ワークロードのアクセスパターンを特定し、モデルにマッピングした上で候補サービスを絞り込み、一貫性・レイテンシ・スケール・ガバナンス・コストの観点で評価する手順を提示している。
