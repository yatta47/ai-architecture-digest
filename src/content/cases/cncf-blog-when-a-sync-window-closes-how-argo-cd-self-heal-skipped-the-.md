---
type: guidance
title: Argo CDの同期ウィンドウ後にself-healがマイグレーションフックを飛ばす競合
title_original: 'When a sync window closes: how Argo CD self-heal skipped the migration hook'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/11/20/when-a-sync-window-closes-how-argo-cd-self-heal-skipped-the-migration-hook/
published_at: '2026-11-20'
---

## 概要

Argo CDで拒否同期ウィンドウ中にリリースを積むと、ウィンドウ明けにself-healが先に走り、Syncフックのマイグレーションが実行されない競合が起きる。再現ラボと原因の解説記事。
