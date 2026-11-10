---
type: guidance
title: AWS Cloud WANでメンテ中も最寄り出口ルーティングを維持するDeepLの事例
title_original: How DeepL keeps closest-exit routing during maintenance with AWS Cloud WAN
ai_relevant: false
company: DeepL
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-deepl-keeps-closest-exit-routing-during-maintenance-with-aws-cloud-wan/
published_at: '2026-11-09'
---

## 概要

DeepLはAWS Cloud WANとDirect Connectゲートウェイを使い、AS_PATH prependで保守対象リンクのリージョンのみを迂回させる。
