---
type: announcement
title: GitHubが高負荷時にHTTPS経由のgit操作へ一時的に認証を求める
title_original: Some Git over HTTPS may temporarily require authentication
ai_relevant: false
company: GitHub
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-19-some-git-over-https-may-temporarily-require-authentication
published_at: '2026-10-19'
---

## 概要

GitHubは異常なトラフィック時に、公開リポジトリへのHTTPS経由のcloneとfetchで一時的に認証を求めることがある。認証済み操作、SSH、push、Web/APIは影響を受けず、自動化にはGITHUB_TOKENやGitHub App、PATの利用が推奨される。
