---
type: announcement
title: ノーコードAIアプリ生成ツール「GitHub Spark」提供終了と移行対応
title_original: Upcoming deprecation of GitHub Spark on GitHub.com
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
source_url: https://github.blog/changelog/2026-08-04-upcoming-deprecation-of-github-spark-on-github-com
published_at: '2026-08-04'
---

## 概要

GitHubは2026年8月4日付でアイデアから短時間でアプリを生成できるノーコードツール「GitHub Spark」への新規登録・新規アプリ作成を停止し、既存ユーザーも8月31日までにアプリのエクスポートが必要になると発表した。デプロイ済みアプリはSpark終了後も動作を続けるが、Sparkのllm()関数が利用していた推論基盤「GitHub Models」は7月30日に既に終了しており、llm()を使うアプリは自前の推論プロバイダーとAPIキーへの切り替えが必要となる。GitHubはCopilotやVS Code、Copilot CLIなど既存の開発ワークフローへの統合が進んだことを理由に、Spark単体の提供を縮小する方針を示している。
