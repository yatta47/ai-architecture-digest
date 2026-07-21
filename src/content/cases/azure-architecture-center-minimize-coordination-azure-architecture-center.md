---
type: guidance
title: 調整を最小化してスケーラビリティを高める分散システム設計原則
title_original: Minimize coordination
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/minimize-coordination
published_at: '2026-06-03'
---

## 概要

複数インスタンスが共有状態に同時アクセスする際のロック競合がスケールの足かせになる問題を取り上げ、非同期のイベント連携、CQRSやイベントソーシング、パーティショニング、冪等な操作設計、楽観的並行性制御、リーダー選出など、ノード間の調整を減らしてスケーラビリティを高める設計パターンをまとめる。
