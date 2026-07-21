---
type: guidance
title: Cache-Asideパターン:キャッシュミス時にオンデマンドでデータストアから読み込む設計
title_original: Cache-Aside pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside
published_at: '2026-07-02'
---

## 概要

読み取り/書き込みスルー機能を持たないキャッシュに対して、アプリケーション側でキャッシュミス時にデータストアから読み込みキャッシュへ格納するCache-Asideパターンを解説。有効期限設定・エビクション・書き込み後の一時的な不整合などの考慮点を整理する。
