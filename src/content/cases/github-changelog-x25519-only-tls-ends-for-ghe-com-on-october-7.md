---
type: announcement
title: GHE.com（データレジデンシー版）でのX25519専用TLS接続の受付終了
title_original: X25519-only TLS ends for GHE.com on October 7
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
source_url: https://github.blog/changelog/2026-09-30-x25519-only-tls-ends-for-ghe-com-on-september-15
published_at: '2026-09-30'
---

## 概要

2026年10月7日以降、データレジデンシー付きGitHub Enterprise Cloudは、鍵共有にX25519のみを提示するクライアントからのTLS接続を受け付けなくなる。対象エンドポイントはFIPS承認のP-256・P-384を引き続きサポートし、多くの利用者は対応不要だが、X25519専用に設定されたアプリ・プロキシ・TLSライブラリは設定変更が必要となる。SSH接続には影響しない。
