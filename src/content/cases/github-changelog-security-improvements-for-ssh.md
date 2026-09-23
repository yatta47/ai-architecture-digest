---
type: announcement
title: GitHubのSSHセキュリティ強化(SHA-1 RSA廃止・ML-KEM追加)
title_original: Security improvements for SSH
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
source_url: https://github.blog/changelog/2026-09-22-security-improvements-for-ssh
published_at: '2026-09-22'
---

## 概要

GitHubはSHA-1のRSA署名とdiffie-hellman-group-exchange-sha256の廃止、2026年10月14日以降の新規RSA鍵を3072ビット以上に、ポスト量子鍵交換mlkem768x25519-sha256の追加を発表した。HTTPSでアクセスする場合は影響しない。
