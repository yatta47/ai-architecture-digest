---
type: announcement
title: VS Code Agentsウィンドウの利用状況をCopilotメトリクスに追加
title_original: Add VS Code Agents to Copilot usage metrics
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
components:
- GitHub Copilot
- VS Code Agents
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-11-add-vs-code-agents-to-copilot-usage-metrics
published_at: '2026-09-11'
---

## 概要

GitHubはCopilot利用状況メトリクスに、VS Code Agentsウィンドウ専用のアクティブユーザー数・セッション数・メッセージ数の指標を追加した。企業・組織の管理者はこれによりVS Code Agentsウィンドウの採用状況と利用度を、エディタ内Agent Modeとは区別して追跡できるようになる。

## 設計のポイント

- 新しい利用面（VS Code Agentsウィンドウ）を既存の集計指標と混在させず独立したオプションフィールドとして追加し後方互換性を保つ

## 使いどころ

- エンタープライズ管理者がAIコーディングエージェント機能ごとの採用率を分けて可視化したい場合
