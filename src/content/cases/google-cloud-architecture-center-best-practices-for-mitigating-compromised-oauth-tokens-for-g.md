---
type: guidance
title: gcloud CLIのOAuthトークン漏えい対策のベストプラクティス
title_original: Best practices for mitigating compromised OAuth tokens for Google Cloud CLI
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
source_url: https://docs.cloud.google.com/architecture/bps-for-mitigating-gcloud-oauth-tokens
published_at: '2026-07-25'
---

## 概要

gcloud CLIのOAuthトークンが窃取された場合の影響を抑えるためのベストプラクティス。短命かつコンテキスト認識型の認証情報の利用や、侵害後の失効・監査手順を解説する。
