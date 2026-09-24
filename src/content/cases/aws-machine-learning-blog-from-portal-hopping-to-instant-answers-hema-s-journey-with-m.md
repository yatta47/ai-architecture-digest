---
type: case
title: 社内ナレッジをMCPで各ツールに届けるAIアシスタントHAL
title_original: 'From portal-hopping to instant answers: HEMA''s journey with MCP and Amazon Bedrock'
company: HEMA
industry: retail
cloud:
- aws
patterns:
- ai-agent
- rag
- guardrails
- context-engineering
components:
- Amazon Bedrock AgentCore
- AgentCore Gateway
- AgentCore Runtime
- AgentCore Identity
- AgentCore Memory
- Amazon Bedrock Guardrails
- Amazon Bedrock Knowledge Bases
- Strands Agents
- Model Context Protocol
- Microsoft Entra ID
- Next.js
- Kiro
- Claude
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/from-portal-hopping-to-instant-answers-hemas-journey-with-mcp-and-amazon-bedrock/
published_at: '2026-09-23'
---

## 概要

オランダの小売HEMAが、分散していたwikiやサービスカタログなどの社内知識を一元化する社内AIアシスタントHALを、MCPとAmazon Bedrock AgentCoreで構築した事例。知識を一度MCPツールとして公開し、HALチャットやKiro、Claudeなど普段使うツールから利用できる。認証はEntra IDで、クライアントにAWS認証情報を持たせない。

## 設計のポイント

- 各知識源をMCPツールとして一度だけ公開し、複数のクライアントから再実装なしで使えるようにする。
- AgentCore GatewayでOpenAPI仕様やLambdaを直接MCPツール化し、独自MCPサーバーの運用を避ける。
- 静的な知識はBedrockのRetrieve APIでナレッジベースを直接検索し、ライブAPIはMCP経由と、経路を使い分ける。
- Entra ID連携のJWT認証と、既存ADグループによるアクセス制御、現時点は読み取り専用で安全に公開する。

## 使いどころ

- 手順やルールが分散し、オンボーディングに時間がかかる開発組織。
- IDEやチャットから社内ナレッジを引きたいエンジニアリング部門。
- 将来的に参照系アシスタントから実行系（アクション）へ拡張したい企業。
