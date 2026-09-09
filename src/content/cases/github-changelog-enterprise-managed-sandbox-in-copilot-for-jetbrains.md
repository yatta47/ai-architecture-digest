---
type: announcement
title: GitHub Copilot for JetBrainsに企業管理サンドボックスとエージェント連携強化
title_original: Enterprise-managed sandbox in Copilot for JetBrains
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- multi-agent-orchestration
components:
- GitHub Copilot
- JetBrains IDEs
- MCP
- Copilot CLI
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-08-enterprise-managed-sandbox-in-copilot-for-jetbrains
published_at: '2026-09-09'
---

## 概要

GitHub CopilotのJetBrains向けリリースで、管理者がサンドボックスのファイル/ネットワークアクセスなどを一元管理できる企業ポリシー機能が公開プレビューになった。あわせてサブエージェントのモデル選択、MCPサーバーやエージェントセッションの信頼性改善、ターミナルCopilot CLIとIDEの連携なども強化された。

## 設計のポイント

- サンドボックスの管理者設定はユーザー設定より優先され、IDE上でロック表示することで組織のポリシー逸脱を防ぐ
- エージェントハーネス内の組み込みサブエージェントごとに使用モデルを選択可能にし、コスト/品質のトレードオフを制御しやすくする
- /ideコマンドでターミナルのCopilot CLIセッションをIDEの選択範囲・診断情報・ファイル参照と紐付け、コンテキストの分断を防ぐ

## 使いどころ

- エージェント型コーディングツールを組織全体で展開する際にセキュリティ境界を統制したい管理者
- ターミナルとIDEを行き来しながらAIエージェントに作業させたい開発者
- MCPサーバーや複数のサブエージェントを併用する開発チームの信頼性向上
