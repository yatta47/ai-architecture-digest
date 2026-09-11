---
type: announcement
title: シークレット漏えいを含むプルリクエストのマージをルールセットでブロック
title_original: Block pull requests with exposed secrets from merging
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
source_url: https://github.blog/changelog/2026-09-09-block-pull-requests-with-exposed-secrets-from-merging
published_at: '2026-09-09'
---

## 概要

リポジトリルールセットに、シークレットスキャンアラートが未解決のプルリクエストのマージをブロックする新ルールが追加された。プッシュ時点で防ぐpush protectionとは別の層として、PRのヘッドコミットのスキャン完了とアラート未解決の有無をマージ条件にできる。GitHub Secret ProtectionまたはGitHub Advanced Securityの顧客向けにパブリックプレビューとして提供される。
