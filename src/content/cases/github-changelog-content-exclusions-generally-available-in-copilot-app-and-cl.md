---
type: announcement
title: GitHub Copilotアプリ/CLIでコンテンツ除外ポリシーがGA
title_original: Content exclusions generally available in Copilot app and CLI
company: GitHub
industry: cross-industry
cloud: []
patterns:
- guardrails
components:
- GitHub Copilot
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-02-content-exclusions-generally-available-in-copilot-app-and-cli
published_at: '2026-09-02'
---

## 概要

GitHub CopilotアプリおよびCLIが、エンタープライズ・組織・リポジトリ管理者が設定したコンテンツ除外ポリシーを尊重するようになり、エージェント的ワークフローにおいても除外対象ファイルをコンテキストとして使わなくなったことを伝える記事。

## 設計のポイント

- 管理者が設定した除外ポリシーをエージェントのコンテキスト取得層で強制し、機密コードがAIコンテキストに混入しないようにする

## 使いどころ

- 機密性の高いコードを含むリポジトリでAIコーディングアシスタントを組織展開する場合のガバナンス
