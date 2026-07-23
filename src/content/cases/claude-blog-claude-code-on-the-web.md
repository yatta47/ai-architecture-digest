---
type: announcement
title: ブラウザから並行実行できるClaude Code on the web
title_original: Claude Code on the web
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- parallel-execution
components:
- Claude Code
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-code-on-the-web
published_at: '2025-10-20'
---

## 概要

ブラウザからコーディングタスクをClaudeに委任できる新機能「Claude Code on the web」の提供開始を告知。Anthropic管理のクラウド上で複数リポジトリのタスクを並行実行でき、隔離されたサンドボックス環境とセキュアなGitプロキシで安全性を確保している。

## 設計のポイント

- 各セッションを独立したサンドボックス環境で実行し他リポジトリへの越境アクセスを防ぐ
- Gitとのやり取りをセキュアプロキシ経由に限定し認証情報をサンドボックス内に置かない
- カスタムネットワーク設定で許可ドメインを制御し、必要な外部通信のみ許可する

## 使いどころ

- バグ修正や定型タスクをバックグラウンドで並行処理したい開発チーム
- 複数リポジトリにまたがる作業をターミナルを開かず委任したい場合
- モバイルから開発タスクの進行を確認・指示したいエンジニア
