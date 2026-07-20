---
type: guidance
title: Amazon QuickとNVIDIA NeMo Agent Toolkitで構築するサプライチェーンリスク対応エージェント
title_original: Build specialized agent workflows for your business with Amazon Quick and NVIDIA NeMo Agent Toolkit
industry: logistics
cloud:
- aws
patterns:
- ai-agent
- decision-execution
- root-cause-analysis
components:
- Amazon Quick
- Amazon QuickSight
- NVIDIA NeMo Agent Toolkit
- Amazon Bedrock AgentCore
- Amazon Bedrock AgentCore Gateway
- Amazon Bedrock AgentCore Runtime
- Model Context Protocol (MCP)
- Amazon S3
- AWS CloudFormation
- AWS Lambda
- Amazon ECR
- AWS CodeBuild
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-specialized-agent-workflows-for-your-business-with-amazon-quick-and-nvidia-nemo-agent-toolkit/
published_at: '2026-07-20'
---

## 概要

サプライチェーンの供給遅延など異常を検知できても、購買・在庫・契約・物流を横断した対応判断には時間がかかるという課題に対し、Amazon Quickをビジネスユーザー向けのフロントドアとし、NVIDIA NeMo Agent ToolkitでバックエンドのエージェントワークフローをAmazon Bedrock AgentCore経由のMCPアクションとして構築する構成を示す。診断は既存ダッシュボードとナレッジで答え、対応が必要な場面ではMCPアクション経由でNeMoのオーケストレーターが複数ツールを呼び出し、根拠付きの緩和策を返す。

## 設計のポイント

- 業務ユーザー向けのAmazon QuickとバックエンドのNeMo Agent Toolkitワークフローを、AgentCore GatewayのMCPアクションで疎結合に接続する
- 診断(ダッシュボード/ナレッジ参照)とアクション(MCP経由のエージェント呼び出し)の2つのユーザーパターンに分けて設計する
- 登録関数(発注リスク・在庫影響・顧客影響・ポリシー照会・物流オプション・緩和策提案)をワークフロー設定ファイルで宣言的に組み合わせる
- テレメトリ・ステップ別レイテンシ・評価結果を計測し、本番投入前にワークフローとツール選定をチューニングする

## 使いどころ

- データはあるが人手での異常調査に時間がかかるサプライチェーン計画チーム
- 計画担当者を増員せずに受注量拡大に対応したいスタートアップ
- エージェントワークフローの可観測性・評価基盤を整えたいエンジニアリングチーム
