---
type: case
title: マルチテナントAIエージェントのコード実行を多層防御で隔離する仕組み
title_original: How Benchling secured multi-tenant AI agents with Amazon Bedrock AgentCore
company: Benchling
industry: healthcare
cloud:
- aws
patterns:
- ai-agent
- defense-in-depth
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock AgentCore Code Interpreter
- Amazon VPC
- Amazon Route 53 Resolver DNS Firewall
- AWS STS
- Amazon S3
- gVisor
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-benchling-secured-multi-tenant-ai-agents-with-amazon-bedrock-agentcore/
published_at: '2026-09-21'
---

## 概要

ライフサイエンス向けBenchlingは、AIエージェントが生成した科学計算コードを数千テナント規模で安全に実行するため、Bedrock AgentCore Code InterpreterをVPCモードで本番アカウントと分離した専用アカウントに配置した。インターネットゲートウェイ・NATゲートウェイなしのVPCとRoute 53 Resolver DNS Firewallの3段階ポリシーでDNS経由のデータ持ち出しを含むあらゆる不正な通信経路を遮断し、週250テナント・1日600件超のコード実行をゼロインシデントで運用している。

## 設計のポイント

- 未信頼コード実行専用のAWSアカウントを本番アカウントと分離し、万一の侵害でも顧客データやIAMロールを持つ本番環境を直接露出させないスコープ隔離を行う
- テナントごとにIAMロールを持つのではなく、AWS STSでジョブ単位の一時認証情報をセッションに注入し、数千テナント規模でのロールスプロールを回避する
- インターネットゲートウェイ・NATゲートウェイを持たないVPCを起点に、Route 53 Resolver DNS Firewallで明示ブロック→明示許可→残り全ブロックの3段階ポリシーを適用し、システムのデフォルト設定に依存しないDNS制御を実現する
- S3向けのGatewayエンドポイントとInterfaceエンドポイントのみを許可経路とし、NACLとプレフィックスリストでVPCエンドポイント以外への通信を遮断する

## 使いどころ

- 規制の厳しい業界で、多数のテナントの未信頼コード(AIエージェント生成コードを含む)を1つの実行基盤で安全に動かしたい場合
- テナントごとのIAMロール管理を増やさずに、ジョブ単位でデータアクセスをスコープしたい大規模マルチテナントSaaS
- DNSを含むあらゆる経路でのデータ持ち出しを継続的な侵入テストで検証しながら運用したいセキュリティチーム
