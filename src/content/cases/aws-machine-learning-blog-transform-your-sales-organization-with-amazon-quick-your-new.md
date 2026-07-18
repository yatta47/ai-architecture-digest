---
type: announcement
title: 営業サイクル全体を支援するエージェント型AIアシスタント「Amazon Quick」
title_original: 'Transform your sales organization with Amazon Quick: your new agentic AI teammate'
company: Amazon Web Services (AWS)
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- context-engineering
- decision-execution
- human-in-the-loop
components:
- Amazon Quick
- Amazon QuickSight
- Quick Suite
- Quick Space
- Quick Chat
- Microsoft 365
- Outlook
- Microsoft Teams
- Salesforce
- HubSpot
- ServiceNow
- Slack
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/transform-your-sales-organization-with-amazon-quick-your-new-agentic-ai-teammate/
published_at: '2026-07-17'
---

## 概要

AWSは、営業担当者が実際に『売る』ことへ時間を割けるよう、CRM更新・見込み客調査・メール作成といった非中核業務を肩代わりするエージェント型AIアシスタント「Amazon Quick」を紹介している。CRM・メール・Web解析・サポートシステムに接続してエンゲージメント信号を分析し、購買意欲順にリードをランク付け、パーソナライズされたアウトリーチ作成、商談前の1枚資料・提案デッキ生成、日次のアクティビティ要約まで営業サイクル全体を横断して支援する。ブラウザ・デスクトップアプリのほか、Microsoft 365・OutlookやTeamsのサイドパネルからも利用できる。

## 設計のポイント

- スキルは、複数ソースからデータを収集して成果物を生成する再利用可能なワークフローとして定義し、名前呼び出しと条件成立時の自動実行で全アカウントへ横展開する
- 回答・成果物の根拠は、QuickSightダッシュボードやQuick Space（集約ナレッジリポジトリ）など接続済みの最新データに置く
- メール送信・デッキ生成の前にセラーによるレビュー承認をhuman-in-the-loopとして必須にし、鮮度と信頼性を担保する

## 使いどころ

- 手作業のCRM更新・見込み客調査・商談準備に追われ、大量のリードから優先順位を付けきれない営業チームや担当者に効く
- 既存のSalesforce/HubSpot/Microsoft 365環境にアシスタントを重ねて『売る時間』を取り戻したい組織に向く
