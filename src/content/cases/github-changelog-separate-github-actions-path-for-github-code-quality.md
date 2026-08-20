---
type: announcement
title: GitHub Code QualityのActionsワークフローパスをCode Scanningから分離
title_original: Separate GitHub Actions path for GitHub Code Quality
ai_relevant: false
company: GitHub
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-20-separate-github-actions-path-for-github-code-quality
published_at: '2026-08-20'
---

## 概要

GitHub Code QualityのCodeQL Actionsワークフローが、Code Scanningと共有していた実行パス/アクター名から分離され、dynamic/github-code-quality/codeqlという専用パスとgithub-code-qualityアクターで実行されるようになった。ワークフロー実行履歴やActions利用状況レポートでCode QualityとCode Scanningの実行を区別できる。
