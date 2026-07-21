---
type: case
title: Claude Cowork によるマーケティング業務の自動化(週次レポート・イベント設営)
title_original: How Anthropic's marketing operations team uses Claude Cowork to automate reporting and campaign builds
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- human-in-the-loop
components:
- Claude Cowork
- Salesforce
- HubSpot
- Swoogo
- Asana
- Slack
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-anthropics-marketing-operations-team-uses-claude-cowork-to-automate-reporting-and-campaign-builds
published_at: '2026-07-08'
---

## 概要

Anthropicのマーケティングオペレーションチームは、週次レポート作成と新規イベント設営という手作業中心の業務をClaude Coworkで自動化した。スケジュールタスクとディスパッチャースキルが定型作業を担い、担当者は検証と例外対応に集中できるようになった。

## 設計のポイント

- スケジュールタスクが週次でデータ収集・整形を先行実行し、担当者は月曜朝に結果をレビューするだけで済む構成にした
- ディスパッチャースキルはルーティングのみを担当し、実際の作業は5つの専門スキルに分離することで、個々のスキルを独立して改善できるようにした
- 数値が既存の集計と食い違う場合はモデルが推測せず人に確認を求めるフローを組み込み、誤った数字が報告に混入しないようにした
- セッション終了時に得られた知見をスキルへフィードバックし、継続的にプロンプト/スキルを更新する仕組みを設けた

## 使いどころ

- 複数のSaaSツール(CRM・自動化基盤・イベント管理ツール等)をまたぐ定型業務を抱えるマーケティングオペレーション担当者
- 週次・月次のレポーティングに多くの時間を取られているアナリストやマネージャー
- リクエストの受付から実行までを一定の型で回したいキャンペーン/イベント運営チーム
