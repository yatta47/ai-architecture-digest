---
type: guidance
title: MCPコネクタとAgentCoreで実現する製造業向け自律型BIエージェント
title_original: Generate Autonomous Business Insights with AI Agent and MCP Servers
industry: manufacturing
cloud:
- aws
patterns:
- ai-agent
- data-federation
- business-intelligence-resilience
- text-to-sql
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock
- Amazon SageMaker Lakehouse
- Amazon SageMaker Data Catalog
- Amazon Redshift
- AWS S3 Tables
- Amazon Aurora PostgreSQL
- Amazon OpenSearch Service
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/generate-autonomous-business-insights-with-ai-agent-and-mcp-servers/
published_at: '2026-07-29'
---

## 概要

製造ラインの管理者が5〜8個の異なるシステムを手作業で突き合わせていたBI分析を、Amazon Bedrock AgentCoreを中心とした自律型エージェント基盤に置き換える参照アーキテクチャ。事前構築MCPサーバコネクタとセマンティックレイヤー(SageMaker Data Catalog)により、コーディング無しで複数データソースを横断した自然言語での意思決定支援を実現する。役割ごとのアクセス権限は平文のポリシールールとして定義される。

## 設計のポイント

- セマンティックレイヤー(SageMaker Data Catalog)でデータ発見とデータ取得を分離し、新規ソースの追加を登録だけで完結させる
- 事前構築MCPサーバコネクタ(Redshift/S3 Tables/Aurora等)により個別データストアへのカスタム統合コードを排除する
- Bedrockで自然言語の意図分類とレスポンス合成を行い、AgentCoreがオーケストレーション・認可・メモリを一元管理する
- アクセス制御を平文のポリシールールとして定義し、AgentCoreが実行時の認可ロジックへ変換する

## 使いどころ

- 複数の運用・分析システムに跨るデータを手作業で突き合わせている生産管理者の意思決定支援
- 役職やアクセス権限が異なる複数の現場担当者が同じデータ基盤に自然言語で質問したい組織
- 月〜週次の定例レビュー前に根本原因分析まで含めた洞察を短時間で得たい製造オペレーション
