---
type: guidance
title: Bedrockマネージドナレッジベースで作るエージェント型検索をCDKで一括構築
title_original: Build agentic retrieval on a Managed Amazon Bedrock Knowledge Base with CDK
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- rag
- ai-agent
- eval
- llmops
components:
- Amazon Bedrock Knowledge Bases
- Amazon Bedrock AgentCore
- AgenticRetrieveStream
- AWS CDK
- Amazon CloudWatch
- Amazon S3
- Model Context Protocol
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-agentic-retrieval-on-a-managed-amazon-bedrock-knowledge-base-with-cdk/
published_at: '2026-10-26'
---

## 概要

単発の検索と生成では複数コーパスにまたがる質問や再検索が必要な質問に答えきれない。Managed Knowledge BaseとAgentCoreのGatewayとRuntimeを使い、複数ナレッジベースを渡り歩く推論エージェントを、7層のテレメトリと評価込みで1つのCDKアプリとして構築する手順を示す。

## 設計のポイント

- 各ナレッジベースをGatewayでMCPツールとして公開し、エージェントが検索の要否と対象を判断してループで再検索する。
- Managed Knowledge Baseに取り込み・保存・検索を任せ、ベクトルストアの自前運用をなくす。
- CloudWatchダッシュボード2枚と、オンデマンドおよび継続の評価を同じデプロイで用意し、観測性を設計に組み込む。
- CDKが依存順序を導出し、1コマンドでデプロイする。

## 使いどころ

- 複数の社内文書群にまたがる質問へ根拠付きで答える社内検索を作りたいチーム。
- 経路が質問ごとに変わるエージェントの挙動と回答品質を可視化したい運用担当。
- 従来のRAG構成を管理型サービスへ移行したい場面。
