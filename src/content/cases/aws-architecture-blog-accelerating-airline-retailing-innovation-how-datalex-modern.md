---
type: case
title: 'Datalexの航空リテールシステム刷新: EBAとエージェント型AIでJava移行とエージェントPoCを3日で実施'
title_original: 'Accelerating airline retailing innovation: how Datalex modernized with AWS Experience-Based Acceleration
  and agentic AI'
company: Datalex
industry: logistics
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- ci-cd
components:
- Kiro
- AWS Transform Custom
- Amazon Q Developer
- Amazon Bedrock AgentCore
- Amazon ECS
- Amazon ECR
- AWS Security Hub
- Amazon CloudWatch
- Datadog
- Amazon Cognito
- Kong API Gateway
outcome:
  type: speed
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/accelerating-airline-retailing-innovation-how-datalex-modernized-with-aws-experience-based-acceleration-and-agentic-ai/
published_at: '2026-10-01'
---

## 概要

航空会社向けEコマースを提供するDatalexは、AWSの3日間のExperience-Based Acceleration(EBA)ワークショップで、EJB2/Java 8のシステムからSpring/Java 21への移行可能性を実証した。マイクロサービス試作、DevSecOpsパイプライン、QA・可観測性、エージェント型AIのPoCの4ワークストリームを並行して進め、KiroやAWS Transform Customなどで変更を自動化した。AgentCoreによる予約照会の自然言語インターフェースも試作している。

## 設計のポイント

- 互換ランタイムを用意して既存コードを最小限の変更で動かし、残りの変更をAIコーディング支援で自動化した。
- Strangler Figパターンのゲートウェイで既存APIと新APIを切り替え、非回帰テストを素早く行えるようにした。
- CI/CDにセキュリティスキャンを各段階で組み込むシフトレフトを採用した。
- 認証、データ取得、レポートの専門エージェントをAgentCoreで協調させ、Cognito、Kong経由で既存REST APIにつないだ。

## 使いどころ

- 長年稼働する基幹システムを無停止で段階的に近代化したい事業者。
- レガシーなJavaのフレームワーク移行をAIコーディングツールで加速したいチーム。
- 既存APIの上に自然言語エージェント層を重ねたい場合。
