---
type: announcement
title: GitHub ActionsでNode 20が廃止されNode 24へ移行
title_original: Node 20 is no longer available in GitHub Actions
ai_relevant: false
company: GitHub
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-23-node-20-is-no-longer-available-in-github-actions
published_at: '2026-09-23'
---

## 概要

GitHub Actionsのランナーで Node 20 が最終的に利用不可となり、JavaScriptアクションはNode 24で動作するようになった。一時的なオプトアウト設定も廃止され、アクション作成者は runs.using を node24 に更新して再リリースする必要がある。macOS 13.4以前やARM32のセルフホストランナーは非対応になる。
