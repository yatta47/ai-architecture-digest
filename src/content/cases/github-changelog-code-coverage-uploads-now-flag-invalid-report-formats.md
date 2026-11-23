---
type: announcement
title: GitHub Code Qualityのカバレッジ upload がCobertura形式以外を検出して失敗
title_original: Code coverage uploads now flag invalid report formats
ai_relevant: false
company: GitHub
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-23-code-coverage-uploads-now-flag-invalid-report-formats
published_at: '2026-11-23'
---

## 概要

GitHub Code Qualityのupload-code-coverageアクションが、レポートがCobertura XMLでない場合にエラーで失敗するようになった。従来は成功に見えてPRにカバレッジが表示されなかった。有効なレポートに対する処理も寛容になり、行番号などが不正な行のみをスキップする。
