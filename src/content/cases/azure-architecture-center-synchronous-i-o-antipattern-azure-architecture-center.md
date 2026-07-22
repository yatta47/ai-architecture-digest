---
type: guidance
title: 同期I/Oによるスレッドブロッキングのアンチパターン
title_original: Synchronous I/O antipattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/antipatterns/synchronous-io/
published_at: '2026-05-06'
---

## 概要

データベースアクセスや外部サービス呼び出しなどのI/Oを同期的に行うと呼び出しスレッドがブロックされ、処理能力を無駄にしてスケーラビリティを損なうアンチパターンを解説する。ライブラリの制約や『応答が必要だから』という思い込みが原因になりやすく、非同期I/Oへの置き換えを推奨する。
