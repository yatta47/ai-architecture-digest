---
type: announcement
title: GitHub Actions実行履歴クエリの件数表示を2,500+に上限化
title_original: Changes to query results in the GitHub Actions API and UI
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
source_url: https://github.blog/changelog/2026-09-25-changes-to-query-results-in-the-github-actions-api-and-ui
published_at: '2026-09-25'
---

## 概要

GitHub Actionsのワークフロー実行の検索で、該当件数が2,500を超える場合は正確な件数ではなく「2,500+」と表示するようになった。タイムアウト時に不正確な件数が返る問題を避けるための変更で、取得は最大1,000件のページングのままである。
