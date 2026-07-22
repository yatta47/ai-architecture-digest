---
type: guidance
title: ETLとELT、データパイプライン設計の使い分けガイド
title_original: Extract, transform, and load (ETL)
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl
published_at: '2026-03-27'
---

## 概要

ETL/ELTはデータ統合の代表的な2方式であり、変換処理をどこで行うか（専用エンジンか、ターゲットのデータストアか）で使い分けが分かれる。パイプラインは制御フローとデータフローの組み合わせで構成され、抽出・変換・ロードを並列実行することで処理時間を短縮できる。近年は分析基盤から業務システムへデータを戻すリバースETLも普及している。
