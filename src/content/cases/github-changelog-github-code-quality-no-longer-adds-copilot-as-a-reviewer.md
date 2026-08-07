---
type: announcement
title: Code Quality有効化時にCopilotレビューを自動追加する挙動を廃止
title_original: GitHub Code Quality no longer adds Copilot as a reviewer
company: GitHub
industry: cross-industry
cloud: []
patterns: []
components:
- GitHub Copilot
- GitHub Code Quality
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-07-github-code-quality-no-longer-adds-copilot-as-a-reviewer
published_at: '2026-08-07'
---

## 概要

GitHubは、Code Quality機能を有効化した際に自動生成されていた「すべてのプルリクエストにCopilotレビューを要求する」ルールセットの自動作成をやめ、既存の該当ルールセットも設定を無効化した。ユーザーからの「レビュアー追加は自分たちで選択したい」というフィードバックを受けた変更で、自動Copilotレビューを引き続き使いたい場合はルールセットで明示的に有効化する必要がある。

## 設計のポイント

- 自動で有効化していた挙動をユーザーが明示的にオプトインする設計に変更し、ユーザーが独自に編集したルールセットには一切手を加えない

## 使いどころ

- 組織やリポジトリ単位でCopilotレビューの自動要求を選択制にしたい管理者
