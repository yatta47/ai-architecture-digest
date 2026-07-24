---
type: guidance
title: フロントエンドごとに専用バックエンドを用意するBackends for Frontendsパターン
title_original: Backends for Frontends pattern
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends
published_at: '2025-05-15'
---

## 概要

デスクトップとモバイルなど複数のフロントエンドが単一の汎用バックエンドを共有すると、更新の競合やチーム間のボトルネックが生じる問題に対し、フロントエンドごとに専用のBFFサービスを設ける設計パターンを解説する。適用すべき場面と避けるべき場面、信頼性・保守性へのトレードオフを整理する。
