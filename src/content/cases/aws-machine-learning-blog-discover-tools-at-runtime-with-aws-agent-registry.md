---
type: case
title: AWS Agent Registryでエージェントがツールを実行時に発見する構成
title_original: Discover tools at runtime with AWS Agent Registry
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- context-engineering
components:
- AWS Agent Registry
- Amazon Bedrock AgentCore
- MCP
- A2A
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/discover-tools-at-runtime-with-aws-agent-registry/
published_at: '2026-10-20'
---

## 概要

ツールをビルド時に埋め込む代わりに、オーケストレーターがAgent RegistryからMCPサーバーやエージェントを検索して実行時に接続する構成を解説する。Discover→Instantiate→Executeのループで、ツール追加時のオーケストレーター再デプロイを不要にする。

## 設計のポイント

- ツール数が数十を超えるとツール名の曖昧さ解消にトークンを浪費するため、カタログ化して関連ツールだけを検索で取得する。
- 検索結果には認証情報や認証方式を含めず、記述子とエンドポイントから都度クライアントを構築して権限を分離する。
- 公開チームとオーケストレーターのリリースを分離し、各チームが独立して機能を出せるようにする。

## 使いどころ

- 社内に数百のAPIがあり、エージェントへの結線が開発のボトルネックになっている企業。
- 複数チームがMCPサーバーやエージェントを個別に公開するSaaS/プラットフォーム。
