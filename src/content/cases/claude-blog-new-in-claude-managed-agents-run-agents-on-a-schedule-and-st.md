---
type: announcement
title: Claude Managed Agentsにスケジュール実行と認証情報Vaultを追加
title_original: 'New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- scheduled-agent-execution
- defense-in-depth
components:
- Claude Managed Agents
- Vaults
- MCP
- Browserbase
- KERNEL
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/whats-new-in-claude-managed-agents
published_at: '2026-06-09'
---

## 概要

Claude Managed Agentsにスケジュールデプロイメントと環境変数Vaultという2つの新機能がパブリックベータで追加された。スケジュールデプロイメントはcron設定でエージェントを定期起動し、起動のたびに新しいセッションで定型タスク(週次レポート作成、夜間データ同期、本番ログ監視など)を実行し、独自のスケジューラを構築・運用する必要をなくす。Vaultsはサンドボックスにプレースホルダーのみを保持させ、実際のAPIキーは許可されたドメイン宛のリクエスト時にネットワーク境界で注入することで、モデル自身にキーを見せずにCLIや外部サービスを安全に呼び出せるようにする。Rakuten、Actively AI、Ando、Notion、Browserbase、KERNEL、Milanaなどが、自前で構築していたスケジューリング基盤の置き換えや、認証情報を安全に扱うエージェント運用にこれらの機能を利用している。

## 設計のポイント

- スケジュールデプロイメントは起動のたびに新しいセッションを開始する設計にし、ユーザー側で専用スケジューラを構築・運用する必要をなくしている。
- Vaultsではサンドボックス内にプレースホルダーのみを保持し、実際のAPIキーは許可ドメイン宛のリクエスト時にネットワーク境界で注入することで、モデル自身に秘密情報を渡さない構成にしている。
- キーはAPIキー名と到達可能ドメインの組で登録するため、CLI・ツールがアクセスできる範囲を最小権限に絞り込める。
- Vault内のキーを更新すると、実行中のセッションも次回呼び出しから新しい値を自動的に取得する。

## 使いどころ

- 週次・月次のレポート作成や、ダッシュボードを作らずに本番ログ・メトリクスを監視したいチーム(Rakutenの事例)。
- 自前で構築していたスケジューリング基盤を置き換え、社内向け検索・分析システムをシンプルにしたい場合(Actively AIの事例)。
- APIトークンをモデルに渡さずCLI経由で社内システムやSaaSへ安全にアクセスさせたい、セキュリティ要件の厳しいチーム(Notion、KERNELの事例)。
- 複数の営業・採用プロセスを1つの自律エージェントに横断的に監視・フォローアップさせたいチーム(Andoの事例)。
