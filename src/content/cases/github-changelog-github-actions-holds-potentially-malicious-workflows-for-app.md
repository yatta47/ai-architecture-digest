---
type: announcement
title: GitHub Actionsが疑わしいワークフローの実行を承認制で保留
title_original: GitHub Actions holds potentially malicious workflows for approval
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
source_url: https://github.blog/changelog/2026-07-28-github-actions-holds-unproven-workflows-for-approval
published_at: '2026-07-28'
---

## 概要

侵害されたGitHub資格情報を使ってCI/CD認証情報を盗むサプライチェーン攻撃対策として、GitHub Actionsは疑わしいワークフロー実行を自動検知し書き込み権限を持つコラボレーターの承認があるまで保留する機能を公開リポジトリ向けに導入した。設定不要で自動適用される。
