---
type: guidance
title: 監視・ロギングなど周辺機能を別コンテナに切り出すSidecarパターン
title_original: Sidecar pattern
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/sidecar
published_at: '2026-02-18'
---

## 概要

監視・ロギング・設定管理といった周辺機能を、メインアプリケーションと同じホスト上の別プロセス・コンテナとして切り出すSidecarパターンを解説する。言語非依存で共通機能を提供できる利点と、レイテンシやスケーリングの制約とのトレードオフを示す。
