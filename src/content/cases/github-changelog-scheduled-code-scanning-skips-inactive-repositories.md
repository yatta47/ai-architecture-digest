---
type: announcement
title: GitHubの定期コードスキャンが非アクティブなリポジトリをスキップ
title_original: Scheduled code scanning skips inactive repositories
ai_relevant: false
company: GitHub
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: cost
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-01-scheduled-code-scanning-skips-inactive-repositories
published_at: '2026-10-01'
---

## 概要

code scanningのデフォルト設定とGitHub Code Qualityの週次定期スキャンが、pushまたはプルリクエストによる解析の後にのみ開始されるようになった。従来は初回の検証スキャンなども活動と数えられ、休眠リポジトリが半年間アクティブ扱いになっていた。多数のリポジトリへ一括展開した際の想定外の定期スキャンが減る。設定変更は不要で、GitHub Enterprise Cloudで利用でき、Enterprise Server 3.24で対応予定。
