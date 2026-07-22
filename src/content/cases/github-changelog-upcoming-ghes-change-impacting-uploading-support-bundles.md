---
type: announcement
title: GitHub Enterprise Serverのサポートバンドルアップロードにおけるセキュリティ変更
title_original: Upcoming GHES change impacting uploading support bundles
ai_relevant: false
company: GitHub
industry: cross-industry
cloud:
- on-prem
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-22-upcoming-ghes-change-impacting-uploading-support-bundles
published_at: '2026-07-22'
---

## 概要

GitHubは2026年8月18日より、必要なセキュリティパッチが未適用の古いGitHub Enterprise Server(GHES)アプライアンスからのコマンドラインでのサポートバンドルアップロードを拒否するようになる。対象コマンドはghe-support-bundle、ghe-cluster-support-bundle、ghe-support-uploadで、影響を避けるには各バージョン系列の最新パッチ(3.21.3、3.20.5、3.19.9、3.18.12、3.17.18など)への更新が必要となる。期限までに更新できない場合はGitHubサポートへの連絡が推奨される。
