---
type: guidance
title: Amazon QuickとOutlookを連携したメール業務のAI自動化
title_original: Integrating Outlook with Amazon Quick for AI-powered email automation
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- document-processing
components:
- Amazon Quick
- Amazon Quick Flows
- Amazon Quick Automate
- Microsoft Outlook
- Microsoft Graph API
- Microsoft Entra
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/integrating-outlook-with-amazon-quick-for-ai-powered-email-automation/
published_at: '2026-09-03'
---

## 概要

生成AIアシスタントAmazon QuickをOutlookとOAuth 2.0連携させ、メールスレッドの要約・返信ドラフト作成・会議準備・タスク抽出などを自動化する手順を紹介する記事。チャットエージェント、ワークフロー（Flows）、複数ステップの自動化（Automate）の3ツールを組み合わせて利用する。

## 設計のポイント

- Microsoft Graph APIとOAuth 2.0でOutlookに接続し、パスワードを保存せず必要な権限のみ付与する
- チャットエージェントが社内ナレッジベースや過去の対応履歴を参照して文脈に沿った返信を作成する
- 定型的なメール処理はQuick Flowsで自動化し、複数システムをまたぐ複雑な処理はQuick Automateでオーケストレーションする

## 使いどころ

- カスタマーサポートでの一貫した返信ドラフト作成による対応時間短縮
- 経営層・秘書向けの長いメールスレッド要約とアクションアイテム抽出
- 営業チームが複数システムを行き来せず価格・競合情報を取得する場面
