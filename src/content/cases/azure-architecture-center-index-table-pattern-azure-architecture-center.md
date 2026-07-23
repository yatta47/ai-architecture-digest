---
type: guidance
title: セカンダリインデックスを持たないデータストアのためのインデックステーブル設計
title_original: Index Table pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/index-table
published_at: '2026-02-05'
---

## 概要

セカンダリインデックスを持たないNoSQLデータストアで、非主キー項目による検索を高速化するためにインデックステーブルを自前で構築する設計パターンを解説する。完全非正規化・正規化(ファクトテーブル参照)・部分正規化の3方式と、複合キーやシャーディングと組み合わせた活用法を示す。
