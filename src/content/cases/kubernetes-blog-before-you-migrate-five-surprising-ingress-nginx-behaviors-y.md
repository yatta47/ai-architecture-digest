---
type: guidance
title: Ingress-NGINX廃止に向けたGateway API移行時の落とし穴5選
title_original: 'Before You Migrate: Five Surprising Ingress-NGINX Behaviors You Need to Know'
ai_relevant: false
company: Microsoft
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/02/27/ingress-nginx-before-you-migrate/
published_at: '2026-02-27'
---

## 概要

2026年3月に廃止されるIngress-NGINXから移行する際に見落としがちな挙動（正規表現マッチが実は大文字小文字を区別しないプレフィックスマッチである点など）を5つ取り上げ、Gateway APIへの安全な移行方法を解説する。素直な変換だけでは本番障害を招くリスクを具体例で示す。
