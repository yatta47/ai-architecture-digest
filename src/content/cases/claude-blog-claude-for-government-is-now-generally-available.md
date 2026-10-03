---
type: announcement
title: Claude for Governmentが一般提供開始、FedRAMP High環境で提供
title_original: Claude for Government is now generally available
company: Anthropic
industry: public-sector
cloud: []
patterns:
- defense-in-depth
- policy-as-code
components:
- Claude for Government
- Claude Code
- Claude for Microsoft 365
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-for-government-is-now-generally-available
published_at: '2026-09-30'
---

## 概要

連邦・州政府機関向けのClaude for Governmentが一般提供となった。FedRAMP High認可環境でClaudeのコーディング・エージェント機能を提供する。Claude Code CLIとClaude for Microsoft 365は早期アクセス。利用額上限付きの従量課金、SSOやSCIMによる部門別の権限・上限設定、監査ログを備える。

## 設計のポイント

- 席課金を廃し、利用量の固定増分と上限額で支出を制御する。
- SCIMのグループ割り当てで、席の階層ごとにレート上限・金額上限・利用可能モデルを設定する。
- 管理操作を監査ログに残し、ATO手続きを支援する。

## 使いどころ

- 連邦・州機関がAI導入で調達とコンプライアンス要件を満たす場面。
- 部門ごとに利用額を配分しながら統制したい管理者。
