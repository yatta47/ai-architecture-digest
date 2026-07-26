---
type: guidance
title: 高負荷時にも機能を落として動き続ける設計(グレースフルデグラデーション)
title_original: Design for graceful degradation
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/framework/reliability/graceful-degradation
published_at: '2026-07-19'
---

## 概要

高負荷時にシステム全体を落とすのではなく、性能や精度を落としてでも稼働を継続する『グレースフルデグラデーション』の設計原則。スロットリング、フロントエンドでの過剰リクエスト破棄、部分的エラー処理、過負荷シナリオのテストを推奨する。
