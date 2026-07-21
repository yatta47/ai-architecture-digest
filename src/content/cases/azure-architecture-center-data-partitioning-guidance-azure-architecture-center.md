---
type: guidance
title: 大規模データストアのパーティショニング設計ガイド
title_original: Data partitioning guidance
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/best-practices/data-partitioning
published_at: '2026-06-03'
---

## 概要

大規模システムにおけるデータパーティショニングについて、水平分割（シャーディング）、垂直分割、機能分割という3つの代表的な戦略とその組み合わせ方を整理したガイド。スケーラビリティやパフォーマンスの向上、セキュリティ強化、運用の柔軟性、可用性向上といった目的別に各戦略の適用場面を解説し、特にシャーディングキーの選定がホットパーティションの回避やスキーマ変更の容易さを左右する重要な設計判断であることを強調している。
