---
type: guidance
title: ingress-nginx終了後のKubernetesネットワーキング移行戦略
title_original: Navigating the Ingress-NGINX Retirement
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/09/navigating-the-ingress-nginx-retirement/
published_at: '2026-07-09'
---

## 概要

2026年3月にKubernetes SIG NetworkのIngress-NGINXコントローラーが終了し、CVE未パッチや機能更新停止のリスクが生じる。既存のIngress APIを維持しつつContourなど別のIngressコントローラーへ横移動する『リフト&シフト』と、ロール分離型のGateway APIへ本格移行する『アーキテクチャ刷新』の2つの移行パスが比較されている。効果は組織の制約や技術的負債の許容度に依存するとし、ingress2gatewayなどのツールと段階的ロールアウトが推奨される。
