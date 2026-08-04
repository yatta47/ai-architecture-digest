---
type: case
title: Bedrock AgentCoreの管理型ブラウザで実現するWebサイト自動インサイト抽出基盤
title_original: Automated web insight extraction with Amazon Bedrock AgentCore
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- event-driven
- rag
- document-processing
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock
- Amazon OpenSearch Serverless
- AWS Lambda
- Amazon S3
- Amazon SQS
- Amazon EventBridge
- Amazon Cognito
- Amazon ECS
- AWS Fargate
- Amazon CloudFront
- Playwright
- Model Context Protocol
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/automated-web-insight-extraction-with-amazon-bedrock-agentcore/
published_at: '2026-08-04'
---

## 概要

複数のWebサイトから手作業で情報収集していた競合分析や市場調査を自動化するため、Amazon Bedrock AgentCoreの管理型ブラウザでJavaScriptレンダリングを含むページ取得を行い、Bedrockでインサイト抽出・埋め込み生成、OpenSearch Serverlessでセマンティック検索を提供するイベント駆動型システムを構築した。RSSフィード監視からコンテンツ収集・AI分析・検索UI/MCPサーバー公開までを疎結合なパイプラインとして実装している。

## 設計のポイント

- コンテンツ収集(ブラウザ自動化)とAI処理をS3アップロードイベント経由のSQSキューで分離し、それぞれ独立してスケールできるようにする
- AgentCoreの管理型ブラウザでPlaywright over CDP接続を使いJavaScript描画済みページを取得することで、サイト構造変更やJS化に強いパイプラインにする
- 1MB超の大きいHTMLはhtml-to-text、それ以下はMozilla Readabilityで前処理し分岐させることでトークン消費を抑えつつAI出力の一貫性を高める
- OpenSearch Serverlessでキーワード検索とベクトル検索の両方を持たせ、収集した知見をハイブリッドに検索可能にする

## 使いどころ

- 競合のブログ・製品発表・プレスリリースを継続的に追跡したい競合インテリジェンス担当者
- 業界ニュースやアナリストレポートから自社に関連する新興トレンドを見つけたい市場調査チーム
- 複数ソースからコンテンツを集約し読者に関連度の高い記事を選別したいコンテンツキュレーション担当者
- 規制当局のWebサイトやニュースの変更を監視したいコンプライアンス担当者
