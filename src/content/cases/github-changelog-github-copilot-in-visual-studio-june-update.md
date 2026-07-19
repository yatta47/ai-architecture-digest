---
type: announcement
title: Visual Studio向けGitHub Copilotの6月アップデート
title_original: GitHub Copilot in Visual Studio June update
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- ci-cd
components:
- GitHub Copilot
- Visual Studio
- Model Context Protocol
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-14-github-copilot-in-visual-studio-june-update
published_at: '2026-07-15'
---

## 概要

Visual Studio向けGitHub Copilotが使用量トラッキングとアラート、MCPサーバーの信頼検証ダイアログ、C++向けモダナイゼーションエージェントのGA化、PRのCopilot Chatへの取り込みなどを追加した6月更新。

## 設計のポイント

- MCPサーバーの設定とアセットのフィンガープリントを起動時に信頼済みベースラインと比較し、変更があれば承認ダイアログを挟む。
- モダナイゼーションエージェントをAutomated(全自動)とGuided(各ステップ確認)の2モードで提供し自動化と人間レビューを両立する。

## 使いどころ

- 大規模なC++資産のMSVCアップグレードを段階的に進めたい開発チーム。
- 更新されたMCPサーバーの改ざんリスクを可視化・承認制にしたいセキュリティ担当者。
