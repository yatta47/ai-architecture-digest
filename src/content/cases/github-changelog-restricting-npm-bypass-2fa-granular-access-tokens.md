---
type: announcement
title: npmの2FAバイパストークンによる機微操作を対話的2FA必須化で封じる
title_original: Restricting npm bypass2FA granular access tokens from sensitive actions
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
source_url: https://github.blog/changelog/2026-07-31-restricting-npm-bypass-2fa-granular-access-tokens
published_at: '2026-07-31'
---

## 概要

npmの granular access token (GAT) が2FAをバイパスする設定の場合、アカウント・組織・パッケージ管理などの機微操作に対話的な2FA認証を新たに必須化。漏洩したbypassトークンによるアカウント乗っ取りの攻撃面を縮小する。
