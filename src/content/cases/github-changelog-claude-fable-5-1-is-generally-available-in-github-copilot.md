---
type: announcement
title: GitHub CopilotへのClaude Fable 5.1提供開始とデータ保持ポリシー設計
title_original: Claude Fable 5.1 is generally available in GitHub Copilot
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- llm-gateway
- guardrails
components:
- GitHub Copilot
- Claude Fable 5.1
- Visual Studio Code
- GitHub Copilot CLI
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-01-claude-fable-5-1-generally-available-in-github-copilot
published_at: '2026-09-01'
---

## 概要

GitHubは、長時間にわたる自律的なコーディングやナレッジワークに強みを持つAnthropicの新モデルClaude Fable 5.1をGitHub Copilotで一般提供開始した。同モデルはAnthropicの安全性分類器を稼働させるためデフォルトでデータ保持が必要になる一方、対象となるエンタープライズ顧客は年内に限りゼロデータ保持での利用が可能で、管理者はCopilot設定でモデルポリシーを明示的に有効化する必要がある。

## 設計のポイント

- モデルごとにデータ保持要件が異なるため既定はオフとし、管理者がモデル単位で明示的にポリシーを有効化するオプトイン設計にしている
- 安全性分類器運用のためのデフォルトのデータ保持と、対象エンタープライズ向けの期間限定ゼロデータ保持を両立させ、将来的な安全監視基盤（EFS）への移行を見据えている
- IDEやCLI、モバイルアプリなど複数クライアントに共通のモデルピッカーからモデルを選択できる統一的なアクセス設計にしている

## 使いどころ

- 長時間にわたる自律的なコーディングタスクや複雑なエージェントワークフローを任せたい開発チーム
- データ保持要件やコンプライアンスを重視するエンタープライズ管理者が段階的にモデルアクセスを許可する場面
