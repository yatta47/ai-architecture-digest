---
type: guidance
title: Cloud Identity/Google Workspace移行のオンボーディング計画の選び方
title_original: Assess onboarding plans
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/identity/assessing-onboarding-plans
published_at: '2026-07-24'
---

## 概要

Cloud IdentityやGoogle Workspaceへの移行時に、Google自身をIdPとするか外部IdPを使うか、既存コンシューマーアカウントを移行するか、フェデレーション設定とアカウント統合のどちらを先に行うかを判断するための意思決定フレームワークを示す。移行対象アカウント数(100件が目安)に応じて、フェデレーションなし/フェデレーションのみ/フェデレーション先行/アカウント統合先行という4つのオンボーディングプランを提示している。
