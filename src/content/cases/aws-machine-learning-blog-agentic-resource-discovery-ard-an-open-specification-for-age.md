---
type: announcement
title: AIエージェント/MCPリソースを横断発見するAWS Agent RegistryとARD仕様
title_original: 'Agentic Resource Discovery (ARD): An open specification for agent discovery'
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- llm-gateway
components:
- AWS Agent Registry
- Model Context Protocol (MCP)
- IAM
- JWT
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/agentic-resource-discovery-ard-an-open-specification-for-agent-discovery/
published_at: '2026-08-24'
---

## 概要

AWSは組織内のエージェント・MCPサーバー・ツールを一元的に検索できる「AWS Agent Registry」と、レジストリ間を横断発見できるオープン仕様「Agentic Resource Discovery (ARD)」を発表した。承認ワークフローによるキュレーションとハイブリッド検索で、散在するAI資産の発見・接続を効率化する。ARDはDNSのようにレジストリ同士を連合させ、マルチクラウド/オンプレ/SaaSにまたがる発見を可能にする。

## 設計のポイント

- レジストリを「カタログ作成→パブリッシュ→キュレーション承認→発見」の4段階ワークフローとして設計し、品質・セキュリティ基準を満たす資産だけを検索可能にする
- IAMまたは社内IdPのJWTによる柔軟な認可と、セマンティック検索とキーワード検索を組み合わせたハイブリッド検索を両立させる
- MCPネイティブなエンドポイントとして公開し、既存のMCP対応クライアントからそのまま利用できるようにする
- ローカルレジストリの制御はローカルに残したまま、共通プロトコル(ARD)で連合させることで、移行なしに横断発見を実現する

## 使いどころ

- 複数チームがMCPサーバーやエージェントを個別に構築している組織で、資産の重複開発とサイロ化を防ぎたい場合
- マルチクラウド/オンプレ/SaaSにまたがるエージェント資産を一つの検索体験で発見したい場合
- 承認済みリソースのみを利用可能にすることでガバナンス・コンプライアンス要件を満たしたい場合
