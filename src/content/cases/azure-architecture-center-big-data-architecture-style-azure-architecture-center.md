---
type: guidance
title: 'ビッグデータアーキテクチャスタイル: バッチ処理とストリーム処理を束ねる全体構成'
title_original: Big data architecture style
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/big-data
published_at: '2025-08-06'
---

## 概要

従来型データベースでは扱いきれない規模・複雑さのデータを取り込み・処理・分析するビッグデータアーキテクチャの全体像を解説する。バッチ処理とリアルタイムメッセージ取り込み・ストリーム処理という2つの並行フローと、それらをまとめるオーケストレーション層で構成される。
