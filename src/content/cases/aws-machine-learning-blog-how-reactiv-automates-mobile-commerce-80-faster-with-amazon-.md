---
type: case
title: ShopifyアプリのAIスケジューラをAgentCoreの3エージェント構成で自動化
title_original: How Reactiv automates mobile commerce 80% faster with Amazon Bedrock AgentCore
company: Reactiv
industry: retail
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- memory-consolidation
- event-driven
components:
- Amazon Bedrock AgentCore
- Strands Agents SDK
- Amazon EventBridge
- AWS Lambda
- Amazon DynamoDB
- Amazon Redshift
- Amazon ECR
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-reactiv-automates-mobile-commerce-80-faster-with-amazon-bedrock-agentcore/
published_at: '2026-09-22'
---

## 概要

ShopifyマーチャントのモバイルアプリをAI Schedulerが自然言語指示に基づき自動更新する仕組みを、Reactivはsupervisor・analytics・builderの3エージェント構成でAmazon Bedrock AgentCore上に構築した。対話型エージェントとスケジュール型エージェントを単一スタックに統合し、マーチャント設定時間を80%削減、本番投入も33%高速化した。

## 設計のポイント

- supervisorが意図分類、analyticsがtext-to-SQLでテレメトリ照会、builderが設定生成を担う役割分担型マルチエージェントにした
- AgentCore memoryでセッション要約・好み学習・事実抽出をマーチャント単位にスコープしてセッションをまたぐ文脈を維持した
- 設定スキーマサーバーをAgentCore runtime上でMCPとしてネイティブホストし独自認証層やJSON-RPCハンドシェイクを排除した
- 各マーチャントの実行状態をFirecracker microVMで分離しマルチテナントのデータ隔離をインフラ層で担保した

## 使いどころ

- 多数のテナント向けに定期的なコンテンツ更新を自然言語スケジュールで自動化したいSaaS
- 対話型エージェントと定期実行エージェントを同じメモリ基盤に統合したいプロダクト
- ツール定義やAPI仕様の管理コストを減らしたいマルチエージェント開発チーム
