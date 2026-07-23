---
type: guidance
title: コマンドとイベントの違いから整理する非同期メッセージング設計
title_original: Asynchronous messaging options
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/messaging
published_at: '2026-02-18'
---

## 概要

メッセージを「コマンド」と「イベント」に分類し、メッセージブローカーが提供する疎結合・負荷分散・負荷平準化といった役割を解説する。Azure Service Bus、Event Grid、Event Hubsをメッセージ特性に応じて使い分けるための考え方を示す。
