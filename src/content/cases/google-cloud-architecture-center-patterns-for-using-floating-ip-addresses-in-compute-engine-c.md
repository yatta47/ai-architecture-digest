---
type: guidance
title: オンプレミスのフローティングIPをCompute Engineへ移行するフェイルオーバーパターン
title_original: Patterns for using floating IP addresses in Compute Engine
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
source_url: https://docs.cloud.google.com/architecture/patterns-for-floating-ip-addresses-in-compute-engine
published_at: '2026-07-24'
---

## 概要

オンプレミスで使われるフローティング（仮想）IPアドレスによるフェイルオーバーはCompute Engineでは直接使えないため、ロードバランシング・ルート・オートヒーリングを用いた複数の代替パターンを提示し、移行時にどのパターンを選ぶべきかを解説する。
