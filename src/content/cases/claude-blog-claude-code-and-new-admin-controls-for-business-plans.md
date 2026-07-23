---
type: announcement
title: Claude CodeをBusinessプランに統合し、管理者向け統制とCompliance APIを追加
title_original: Claude Code and new admin controls for business plans
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- Claude Code
- Claude
- Compliance API
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-code-and-new-admin-controls-for-business-plans
published_at: '2025-08-20'
---

## 概要

EnterpriseおよびTeamプランにプレミアムシートを導入し、Claude(対話)とClaude Code(コーディングエージェント)を1つのサブスクリプションに統合した。管理者は組織全体の利用状況を可視化・統制でき、新設のCompliance APIによって利用データや顧客コンテンツへのプログラムアクセスも可能になる。

## 設計のポイント

- 標準/プレミアムの2種類のシートを用意し、ユーザーの役割に応じて管理者が柔軟に割り当てられるようにする
- アイデア出し(Claude)から実装(Claude Code)まで同一サブスクリプション内でシームレスに行き来できるようにする
- Compliance APIで利用データ・顧客コンテンツへのプログラムアクセスを提供し、監査とガバナンスを組織側で完結させる

## 使いどころ

- 開発ライフサイクル全体をClaudeとClaude Codeで一貫して支援したいEnterprise/Teamの開発組織
- AI利用の可視化・統制・監査ログを必要とする情報システム部門やコンプライアンス担当者
