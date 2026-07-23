---
type: guidance
title: クラウドにおける一時的障害への再試行戦略のベストプラクティス
title_original: Best practices for transient fault handling
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/best-practices/transient-faults
published_at: '2026-02-26'
---

## 概要

クラウド環境ではスロットリングや動的なリソース配置により一時的障害が発生しやすいことを説明し、組み込みの再試行機構の活用、リトライ対象の見極め、リトライ回数・間隔の設計指針を示す。カスケード障害を防ぎ広範囲な障害復旧手続きへのエスカレーションを避けることが狙い。
