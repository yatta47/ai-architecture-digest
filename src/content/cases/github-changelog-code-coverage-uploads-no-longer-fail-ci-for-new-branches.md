---
type: announcement
title: GitHub Code Qualityのカバレッジアップロードが新規ブランチでCIを失敗させない
title_original: Code coverage uploads no longer fail CI for new branches
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
source_url: https://github.blog/changelog/2026-10-01-code-coverage-uploads-no-longer-fail-ci-for-new-branches
published_at: '2026-10-01'
---

## 概要

GitHub Code Qualityのupload-code-coverageアクションは、プルリクエストが未作成のブランチにpushした場合、失敗せずアップロードをスキップし、Actionsの通知とステップサマリーで理由を示すようになった。従来はカバレッジAPIがプルリクエスト番号を要求しており、無関係な失敗が起きていた。GitHub Enterprise CloudとTeamで利用でき、Enterprise Serverでは未対応。
