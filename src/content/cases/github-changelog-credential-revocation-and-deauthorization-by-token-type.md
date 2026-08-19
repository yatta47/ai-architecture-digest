---
type: announcement
title: トークン種別ごとの認証情報失効・認可解除機能
title_original: Credential revocation and deauthorization by token type
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
source_url: https://github.blog/changelog/2026-08-18-credential-revocation-and-deauthorization-by-token-type
published_at: '2026-08-18'
---

## 概要

GitHubの認証情報キルスイッチが、これまで全種別一括だった失効操作をPAT・SSH鍵・OAuthアプリトークン・GitHub Appユーザートークンなど種別単位で実行できるようになった。エンタープライズおよび組織レベルのUI・REST APIから侵害の影響範囲を限定した対応が可能になり、操作はすべて監査ログに記録される。
