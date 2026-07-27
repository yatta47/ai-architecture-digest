---
type: guidance
title: バッチ処理をクラウドへ逃がすクラウドバースティングパターン
title_original: Cloud bursting pattern
ai_relevant: false
industry: cross-industry
cloud:
- gcp
- on-prem
patterns: []
components: []
outcome:
  type: cost
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/cloud-bursting-pattern
published_at: '2026-07-21'
---

## 概要

オンプレミス環境をベースロードとして運用し、需要が高まった際にGoogle Cloudへ一時的に処理をバーストさせるハイブリッドアーキテクチャパターン。主にバッチ処理やCI/CDジョブなど瞬間的に負荷が跳ね上がるワークロードを、過剰プロビジョニングなしに吸収することを目的とする。コスト最適化とスケール対応の俊敏性向上が主な狙い。
