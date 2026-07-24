---
type: guidance
title: CQRSパターンで読み取りと書き込みのデータモデルを分離する設計
title_original: Command Query Responsibility Segregation (CQRS) pattern
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs
published_at: '2025-02-21'
---

## 概要

単一データモデルでの読み書き共存が招くデータ不一致・ロック競合・性能劣化・セキュリティ課題を、コマンド（書き込み）とクエリ（読み取り）の責務を分離するCQRSパターンで解消する方法を解説する。同一データストア内でモデルを分ける基本形と、別々のデータストアをイベントで同期する発展形の2アプローチを紹介する。
