---
type: guidance
title: 腐敗防止層（Anti-Corruption Layer）パターン：新旧システム間の意味論的差異を吸収する
title_original: Anti-Corruption Layer pattern
ai_relevant: false
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer
published_at: '2026-05-30'
---

## 概要

セマンティクスの異なる新システムとレガシーシステムの間にファサード/アダプタ層を挟み、モデル変換を一手に引き受けることで新システムの設計をレガシーの制約から守る設計パターン。段階的移行や外部システム連携で有効。
