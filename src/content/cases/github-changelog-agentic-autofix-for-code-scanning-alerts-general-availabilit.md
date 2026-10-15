---
type: announcement
title: CodeQLで検証しながら修正するエージェント型オートフィックス
title_original: Agentic autofix for code scanning alerts general availability
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- ci-cd
- human-in-the-loop
components:
- GitHub Copilot
- CodeQL
- GitHub Actions
- GitHub Code Security
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability
published_at: '2026-10-15'
---

## 概要

GitHubはコードスキャンのアラートをCopilotに割り当てる機能を一般提供した。関連ファイルを調べて修正案を作り、CodeQLを再実行して解消を確認してからドラフトPRを出す。最大25件のアラートを1つのPRにまとめられる。

## 設計のポイント

- 修正後に静的解析を再実行して解消を自己検証する
- 最終的にドラフトPRとして人のレビューに委ねる
- 企業管理者のポリシーで有効化を段階的に制御する

## 使いどころ

- 大量のセキュリティアラートの修正が滞っている開発組織
