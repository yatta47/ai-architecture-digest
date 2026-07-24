---
type: announcement
title: Anthropic API ConsoleのWorkspaces機能
title_original: Workspaces in the Anthropic API Console
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- llmops
- cost-optimization
components:
- Anthropic API Console
- Workspaces
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/workspaces
published_at: '2024-09-10'
---

## 概要

開発/ステージング/本番など複数のClaudeデプロイを管理しやすくするWorkspaces機能をAnthropic API Consoleに追加。ワークスペース単位で支出上限やレート制限、アクセス権限を設定でき、APIキーや利用状況をプロジェクト単位で整理できる。

## 設計のポイント

- 組織全体のレート制限内でワークスペースごとに個別のレート制限・支出上限を設定できる階層構造にする
- APIキー・利用状況・権限をワークスペース単位でグルーピングし環境やプロジェクトごとの管理を容易にする

## 使いどころ

- 開発・ステージング・本番など複数環境でClaudeを使い分けるチーム
- プロジェクトやチームごとにAPIコストを可視化・上限管理したい組織
