---
type: guidance
title: マイクロサービス間通信の設計：同期・非同期とレジリエンスパターン
title_original: Interservice communication in microservices
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/microservices/design/interservice-communication
published_at: '2026-04-20'
---

## 概要

多数のマイクロサービスインスタンス間の通信を堅牢にするため、非同期メッセージングと同期APIのトレードオフ、リトライやサーキットブレーカーといったレジリエンスパターンを解説する。ノード障害やインスタンスクラッシュなど、ネットワーク呼び出しが失敗しうる典型的な要因を整理している。
