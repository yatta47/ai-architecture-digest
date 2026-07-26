---
type: guidance
title: シフトレフト・セキュリティの実装原則
title_original: Implement shift-left security
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
source_url: https://docs.cloud.google.com/architecture/framework/security/implement-shift-left-security
published_at: '2026-07-19'
---

## 概要

Google Cloud Well-Architected Frameworkのセキュリティピラーが提唱する「シフトレフト」原則。IaCやポリシーアズコードをCI/CDパイプラインに組み込み、デプロイ前に予防的統制を効かせ、デプロイ後は脆弱性スキャンとコードレビューで迅速に修正することを推奨する。
