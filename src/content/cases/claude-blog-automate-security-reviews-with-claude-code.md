---
type: announcement
title: Claude Codeに/security-reviewコマンドとGitHub Actions連携でセキュリティレビューを自動化
title_original: Automate security reviews with Claude Code
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- ci-cd
components:
- Claude Code
- GitHub Actions
- /security-review
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/automate-security-reviews-with-claude-code
published_at: '2025-08-06'
---

## 概要

Claude CodeにGitHub Actions連携と新しい/security-reviewコマンドを追加し、SQLインジェクションやXSS、認証・認可の欠陥などの脆弱性検出とその場での修正実装を自動化した。開発の内側のループでセキュリティレビューを行えるようにする。

## 設計のポイント

- コミット前にターミナルからアドホックにセキュリティ分析を実行できる/security-reviewコマンドを用意する
- 脆弱性を検出するだけでなく、その場でClaude Codeに修正実装まで依頼できるようにし、レビューから対応までを一体化する
- GitHub Actions統合により、既存のCI/CDワークフローにセキュリティレビューを組み込めるようにする

## 使いどころ

- 本番到達前に脆弱性を早期発見したい開発チーム
- セキュリティレビューをCI/CDパイプラインに組み込み継続的に実施したいプラットフォームチーム
