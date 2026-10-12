---
type: case
title: HealthOmicsとBedrock AgentCoreによる薬剤耐性遺伝子の対話型サーベイランス
title_original: Agentic antimicrobial resistance surveillance with AWS HealthOmics and Amazon Bedrock AgentCore
company: AWS
industry: healthcare
cloud:
- aws
patterns:
- ai-agent
- text-to-sql
- event-driven
- guardrails
components:
- AWS HealthOmics
- Amazon Bedrock AgentCore
- Strands Agents
- Amazon S3 Tables
- Amazon Athena
- AWS Step Functions
- AWS Fargate
- Amazon DynamoDB
- AWS Glue
- Amazon Bedrock Guardrails
- Amazon Cognito
outcome:
  type: productivity
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/agentic-antimicrobial-resistance-surveillance-with-aws-healthomics-and-amazon-bedrock-agentcore/
published_at: '2026-10-12'
---

## 概要

公開SRAの配列データを取り込み、HealthOmicsのNextflowで品質管理・アセンブリ・耐性遺伝子検出を行い、Iceberg形式のS3 Tablesに格納して、AgentCore上のStrandsエージェントが自然言語でAthenaに問い合わせる参照アーキテクチャ。バイオインフォマティクスの専門知識やSQLが無くても疫学的な質問に答えられる。実証用でありCDKで1コマンドでデプロイできる。

## 設計のポイント

- DynamoDBで処理済みisolateを記録し、定期実行や手動の再投入でも重複処理を避ける。
- 検出結果をhAMRonizationスキーマに正規化し、Glueで冪等にIcebergへマージして再処理時も行を更新にする。
- Athenaを裏にしたツール群を持つエージェントと、Bedrock Guardrailsによる応答の根拠付けでText-to-SQLを安全に提供する。
- 取り込み、処理、保存、問い合わせの各段を疎結合にして一方向に流す。

## 使いどころ

- 疫学研究者や公衆衛生の担当者が専門家に依頼せず耐性遺伝子の分布を調べたいとき。
- ゲノミクスのパイプラインと対話型分析を組み合わせる設計の参考。
