---
type: announcement
title: npmの『ステージのみ』アクセストークンで公開自動化を安全化
title_original: Stage-only npm tokens for safer automation
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
source_url: https://github.blog/changelog/2026-09-18-stage-only-npm-tokens-for-safer-automation
published_at: '2026-09-18'
---

## 概要

npmの新しい粒度アクセストークン権限『Read and write (stage only)』により、自動化ワークフローはバージョンのステージングのみを行い、直接publishする権限を持たないトークンで運用できるようになった。公開はメンテナーが2要素認証でレビュー・承認する必要があり、bypass-2FAトークンによる直接公開廃止（2027年1月予定）に向けた移行手段として位置づけられている。
