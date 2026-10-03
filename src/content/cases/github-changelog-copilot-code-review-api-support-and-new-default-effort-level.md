---
type: announcement
title: CopilotコードレビューがAPI対応、既定の強度はBalancedに
title_original: 'Copilot code review: API support and new default effort level'
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- GitHub Copilot
- GitHub REST API
- GitHub GraphQL API
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-02-copilot-code-review-api-support-and-new-default-effort-level
published_at: '2026-10-02'
---

## 概要

GitHub Copilotのコードレビューを、REST/GraphQL APIから依頼でき、リクエスト単位でレビュー強度を指定できるようになった。既定の強度は2026年9月28日からBalancedに変わり、Liteは設定で選べる。自社スクリプトや社内ツールからレビューを起動できる。

## 設計のポイント

- API経由でレビューを起動できるため、既存の社内ツールやワークフローにAIレビューを組み込める。
- レビュー強度をリクエスト、リポジトリ、組織、企業の各階層で上書きでき、コストと深さを使い分けられる。

## 使いどころ

- PR作成を契機に自動でAIレビューを走らせたい開発チーム。
- 重要度に応じてレビュー強度を切り替えたい組織管理者。
