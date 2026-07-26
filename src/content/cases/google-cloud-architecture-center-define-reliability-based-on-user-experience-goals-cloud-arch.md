---
type: guidance
title: ユーザー体験を基準にした信頼性目標の定義
title_original: Define reliability based on user-experience goals
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
source_url: https://docs.cloud.google.com/architecture/framework/reliability/define-reliability-based-on-user-experience-goals
published_at: '2026-07-19'
---

## 概要

サーバー中心のメトリクス(CPU使用率など)だけでなく、ユーザーのリクエスト成功率やレイテンシといった体験指標を基準に信頼性を測定・定義することを推奨。Cloud Traceなどでユーザージャーニーを分析し、体験に影響するボトルネックを特定する手法を示す。
