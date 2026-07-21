---
type: guidance
title: メッセージブローカーとイベントでエンタープライズシステムを疎結合に統合する
title_original: Use a message broker and events to integrate enterprise systems
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/integration/queues-events
published_at: '2026-07-07'
---

## 概要

基本のエンタープライズ統合アーキテクチャにAzure Service BusとEvent Gridを追加し、同期直接呼び出しではなく非同期メッセージングでバックエンドシステムを統合する構成。Queue-Based Load LevelingやPublisher-Subscriberパターンにより負荷平準化とスケーラブルな連携を実現する。
