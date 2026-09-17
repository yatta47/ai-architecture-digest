---
type: case
title: Wood Mackenzieの全社共通エージェント基盤APEX
title_original: A shared agentic platform for Wood Mackenzie, on Amazon Bedrock AgentCore
company: Wood Mackenzie
industry: other
cloud:
- aws
patterns:
- ai-agent
- unified-runtime
- multi-agent-orchestration
- guardrails
components:
- Amazon Bedrock AgentCore
- Strands Agents
- LangGraph
- LangChain
- Amazon Bedrock Guardrails
- AgentCore Gateway
- AgentCore Identity
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/a-shared-agentic-platform-for-wood-mackenzie-on-amazon-bedrock-agentcore/
published_at: '2026-09-17'
---

## 概要

Wood Mackenzieは、社内向けWoodyや外部顧客向けLens AIなど複数のエージェントアプリが個別にオーケストレーション・ID管理・ガードレールを再実装する非効率を解消するため、Amazon Bedrock AgentCore上に共通エージェント基盤APEXを構築した。フレームワークやモデルを問わず利用できるモデル非依存性と、管理不要な自動スケーリング、ネイティブなガードレール/ID連携により、各チームは差別化ロジックの開発に集中できる。

## 設計のポイント

- 自前運用のOSSフレームワークではなく、マネージド基盤のAgentCoreを採用してスケーリングやガバナンスを標準化した。
- Strands Agents、LangGraph、LangChain等どのフレームワーク・モデルでも接続できる構成にし、モデル切り替えでビジネスロジックを書き換えずに済むようにした。
- 自然言語のポリシーをCedarに変換してAgentCore Gatewayでツール呼び出しをリアルタイムに検査し、開発・コンプライアンス・セキュリティ各チームがコードなしで監査できるようにした。
- 社内ユーザーと社外顧客の双方に同一基盤をID連携済みの権限(エンタイトルメント)で提供し、評価・ガバナンスの穴を一元的にふさいだ。

## 使いどころ

- 社内に複数の独立したAIエージェントアプリが立ち上がり、基盤が重複投資になっている組織。
- モデルプロバイダのロックインを避けつつ複数フレームワークを併用したいプラットフォームチーム。
- エージェントの誤動作を即座に停止できるガバナンス・ID管理を必要とする規制対応が求められる企業。
