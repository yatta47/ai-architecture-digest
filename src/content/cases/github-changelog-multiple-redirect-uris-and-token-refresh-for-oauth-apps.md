---
type: announcement
title: OAuthアプリのリフレッシュトークン対応と複数リダイレクトURI
title_original: Multiple redirect URIs and token refresh for OAuth apps
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
source_url: https://github.blog/changelog/2026-08-14-multiple-redirect-uris-and-token-refresh-for-oauth-apps
published_at: '2026-08-14'
---

## 概要

GitHubはOAuthアプリとGitHub Appプラットフォームにセキュリティ関連の更新を加えた。OAuthアプリは8時間で失効するアクセストークンと6ヶ月有効なリフレッシュトークンによる短命トークン運用にオプトインでき、リダイレクトURIを最大10件まで複数登録できるようになった。また各リダイレクトURIごとにワイルドカードマッチングの有効・無効を明示的に制御できるようになり、単一URI登録アプリで暗黙に有効だった従来の挙動も可視化された。
