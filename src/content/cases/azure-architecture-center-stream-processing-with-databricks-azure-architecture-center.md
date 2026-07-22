---
type: guidance
title: Azure Databricksによるストリーム処理リファレンスアーキテクチャ
title_original: Stream processing with Azure Databricks
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/data/stream-processing-databricks
published_at: '2026-05-07'
---

## 概要

2系統のリアルタイムデータ（配車の運賃・乗車情報）をAzure Event Hubsで取り込み、Azure Databricksで結合・エンリッチ・集計してAzure Cosmos DBに書き込む、取り込み・処理・格納・分析の4段階ストリーム処理パイプラインを示す。Microsoft FabricがCosmos DBのデータをミラーリングし、ETLレスで分析可能にする。
