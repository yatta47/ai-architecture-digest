---
type: case
title: Claude for Small Businessの新ワークフローで6店舗のカフェ運営を1つのビューに統合
title_original: Claude for Small Business launches new workflows, integrations, and training programs
company: Mothership Coffee Roasters
industry: retail
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- event-driven
components:
- Claude Cowork
- Intuit QuickBooks
- Slack
- Salesforce
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-for-small-business-launches-new-workflows-integrations-and-training-programs
published_at: '2026-09-15'
---

## 概要

Claude for Small Businessは43のワークフローと27の新規連携(Shopify、Salesforce、Stripeなど)を追加し、バックオフィス業務だけでなくリード対応や提案書作成など事業成長に関わる業務までClaude Coworkから任せられるようにした。ラスベガスで6店舗のカフェを展開するMothership Coffee Roastersは、POSやQuickBooks、Slack、メールに散在していた数値をClaudeに接続して週次計画のワークスペースとし、全店舗を1つの統合ビューから運営することで店舗利益率を22%まで引き上げた。

## 設計のポイント

- 複数の業務ツールに散在するデータをコネクタ経由でClaudeに接続し、単一の週次ブリーフに集約する
- デフォルトでは送信・投稿・決済の前に人間の承認を挟み、信頼できるワークフローだけをスケジュール実行に切り替える
- コネクタがない場合でもスプレッドシートのアップロードだけでレポート生成を行えるようフォールバックを用意する
- リード対応のようなイベント駆動の業務を「発生したら実行」のワークフローとして定義し人手を介さず一次対応させる

## 使いどころ

- 複数店舗・複数ツールにまたがる数値を一つのダッシュボードで把握したい小規模事業者
- 問い合わせ対応や提案書作成など属人化しがちな営業活動を自動化したいチーム
- エンジニアを持たない事業者がノーコードでAIワークフローを組みたい場合
