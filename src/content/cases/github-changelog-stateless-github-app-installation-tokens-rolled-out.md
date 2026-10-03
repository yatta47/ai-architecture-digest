---
type: announcement
title: GitHub Appのステートレス・インストールトークンへの移行完了
title_original: Stateless GitHub App installation tokens rolled out
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
source_url: https://github.blog/changelog/2026-10-02-stateless-github-app-installation-tokens-rolled-out
published_at: '2026-10-02'
---

## 概要

GitHub Appのインストールトークンが、ステートレスなghs_APPID_JWT形式を既定とする段階展開を完了した。トークンは約520文字に長くなるが、権限・スコープ・有効期限は変わらない。移行用ヘッダーは2026年11月30日に廃止されるため、長さ固定の検証やDB列長などの確認が必要。
