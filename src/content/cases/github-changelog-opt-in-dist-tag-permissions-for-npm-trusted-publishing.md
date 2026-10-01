---
type: announcement
title: npm信頼された公開でdist-tag権限をオプトインで付与可能に
title_original: Opt-in dist-tag permissions for npm trusted publishing
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
source_url: https://github.blog/changelog/2026-09-30-opt-in-dist-tag-permissions-for-npm-trusted-publishing
published_at: '2026-09-30'
---

## 概要

npmのtrusted publishing設定に、OIDCの短期認証情報でdist-tag(latest、next、betaなど)を管理できる「Allow npm dist-tag」権限が追加された。従来はタグ操作のためだけに長期アクセストークンが必要だった。権限は新規・既存設定ともにデフォルトでオフで、オプトインで有効にする。
