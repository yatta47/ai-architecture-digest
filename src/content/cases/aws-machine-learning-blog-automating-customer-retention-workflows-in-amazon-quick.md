---
type: guidance
title: Amazon Quickで構築する解約予兆検知〜引き止めレター自動生成パイプライン
title_original: Automating customer retention workflows in Amazon Quick
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- decision-execution
- document-processing
components:
- Amazon Quick
- Amazon Quick Chat Agent
- Amazon Quick Flows
- Amazon Quick Automate
- Amazon S3
- AWS Lambda
- Amazon API Gateway
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/automating-customer-retention-workflows-in-amazon-quick/
published_at: '2026-07-29'
---

## 概要

CSATスコアと通話トランスクリプトの手作業レビューに5日かかっていた解約予兆対応を、Amazon QuickのDashboard・Chat Agent・Flows・Automateを連結したパイプラインで数分に短縮する構築手順。カスタムMCP Actionで顧客の優先度スコアリングを行い、引き止めレターの生成からS3への配信まで自動化する。

## 設計のポイント

- 構造化KPI(CSAT/FCR/AHT)と非構造化の通話トランスクリプトをChat Agentで組み合わせ、『解約リスクがある』だけでなく『なぜ』を特定する
- Chat Agentでの分析手順をQuick Flowsとして再利用可能な定期/オンデマンド自動化に変換する
- カスタムのスコアリングロジックをMCP ActionとしてLambda+API Gatewayでサーバーレスに拡張する
- Quick Automateで監査証跡・ブレークポイント・ロールベースアクセス制御を備えた多段パイプラインとして実行する

## 使いどころ

- コンタクトセンターの解約予兆を検知しリテンション施策の初動を早めたいカスタマーサクセスチーム
- 分析結果から具体的な引き止めレター生成・配布まで一気通貫で自動化したい運用チーム
