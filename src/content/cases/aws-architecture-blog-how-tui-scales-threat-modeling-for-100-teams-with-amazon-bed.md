---
type: case
title: エージェント型ワークフローによる脅威モデリングの自動化
title_original: How TUI scales threat modeling for 100+ teams with Amazon Bedrock
company: TUI
industry: other
cloud:
- aws
patterns:
- ai-agent
- policy-as-code
- human-in-the-loop
components:
- Amazon Bedrock
- Claude Sonnet 4.5
- Amazon Bedrock AgentCore
- LangGraph
- AWS Lambda
- Amazon DynamoDB
- Amazon S3
- AWS Amplify
- Amazon Cognito
outcome:
  type: productivity
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-tui-scales-threat-modeling-for-100-teams-with-amazon-bedrock/
published_at: '2026-11-05'
---

## 概要

旅行大手TUIが、4人のセキュリティチームで100超のプロダクトチームを支える脅威モデリングを、Bedrockの拡張思考付きエージェントで自動化した事例。AWS Threat Designerを拡張し、社内標準に沿った評価を一貫して適用する。10週間のPoCの後、30日で本番化した。

## 設計のポイント

- STRIDEの脅威抽出と社内標準・ISO 27001へのマッピングをLangGraphのワークフローで自動化する。
- AgentCore runtimeで長時間セッションとセッション単位の隔離を管理型で確保する。
- DynamoDBにワークフロー状態を持たせ、中断からの再開を可能にしている。
- 拡張思考の予算を設定可能にして、分析の深さを調整できる。

## 使いどころ

- セキュリティ担当が少なく、レビュー待ちが滞っている大規模組織。
- 社内標準を一貫して適用する設計レビューを自動化したい場合。
