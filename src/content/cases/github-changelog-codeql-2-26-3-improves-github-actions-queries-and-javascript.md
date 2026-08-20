---
type: announcement
title: CodeQL 2.26.3でGitHub ActionsクエリとJavaScript/TypeScriptのモデリングを改善
title_original: CodeQL 2.26.3 improves GitHub Actions queries and JavaScript modeling
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
source_url: https://github.blog/changelog/2026-08-19-codeql-2-26-3-improves-github-actions-queries-and-javascript-modeling
published_at: '2026-08-19'
---

## 概要

静的解析エンジンCodeQLのバージョン2.26.3は、JavaScript/TypeScript/VueのソースモデリングとGitHub Actionsクエリの精度を改善した。merge_groupイベントの信頼できないデータ認識、Vue Composition APIのフロー追跡、キャッシュポイズニングやコマンドインジェクション系クエリの誤検知低減など、複数の検出精度向上と破壊的変更（SelfHostedQueryモジュールの削除）を含む。
