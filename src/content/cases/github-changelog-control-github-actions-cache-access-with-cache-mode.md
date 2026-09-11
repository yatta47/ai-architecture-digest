---
type: announcement
title: GitHub Actionsのキャッシュアクセスをcache-modeで最小権限化
title_original: Control GitHub Actions cache access with cache-mode
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-10-control-github-actions-cache-access-with-cache-mode
published_at: '2026-09-10'
---

## 概要

GitHub Actionsのキャッシュに対して、ワークフロー/ジョブ単位でread/write/write-only/noneのアクセスモードを設定できるcache-modeが一般提供された。信頼度の低いイベントではデフォルトで読み取り専用にするなど、キャッシュポイズニングを防ぐ最小権限設計を可能にする。
