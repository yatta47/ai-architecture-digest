---
type: guidance
title: Bedrock AgentCoreからクロスアカウントのKnowledge Baseへ安全に接続する2つの実装パターン
title_original: Connect Amazon Bedrock AgentCore to cross-account knowledge bases
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- rag
- text-to-sql
- data-federation
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock Knowledge Bases
- Amazon Redshift Serverless
- Amazon Nova Pro
- Claude Haiku 4.5
- AWS STS
- AWS Lambda
- Amazon Bedrock AgentCore Gateway
- AWS IAM
- Strands Agents SDK
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/connect-amazon-bedrock-agentcore-to-cross-account-knowledge-bases/
published_at: '2026-08-26'
---

## 概要

エージェントを持つAWSアカウントと、Redshift Serverlessを裏付けとするBedrock Knowledge Baseを持つ別アカウントとの間で、データをコピーせずに自然言語の回答を生成する構成を解説する。Knowledge Bases側のリソースポリシーはRetrieveAndGenerateをサポートしないため、ツールがSTSで狭いスコープのIAMロールをアサインしてから呼び出す境界設計を採用する。コード制御可能なStrandsエージェント方式と、宣言的なAgentCoreハーネス方式の2バリアントを比較している。

## 設計のポイント

- RetrieveAndGenerateはクロスアカウントのリソースポリシーで直接許可できないため、ツールがAWS STSで専用の狭いスコープIAMロールをアサインしてから呼び出すことでアカウント境界を保ったまま生成応答を得る
- ソースデータをエージェント側アカウントにコピーせず、Knowledge Base側アカウントに置いたままガバナンスを維持する
- カスタム制御が必要ならコードベースのStrandsエージェント（AgentCoreランタイム＋ローカルMCPサブプロセス）、管理された実行ループで十分ならAgentCore Gateway経由でLambdaツールを呼ぶ宣言的ハーネスを選ぶ、という判断基準を提示している
- エージェントを作る前に、ツール選択や複数ステップ推論、会話状態が本当に必要かを確認し、不要なら直接RetrieveAndGenerateを呼ぶだけのシンプルな構成に留める

## 使いどころ

- マルチアカウント構成のAWS環境で、エージェントのワークロードとガバナンスされたデータのワークロードのアカウント境界を維持したい企業
- Redshift Serverless上の構造化データに対して自然言語で回答を生成しつつ、ソースデータを別アカウントにコピーしたくない場合
- エージェントのオーケストレーションループをどこまで自社でカスタム制御すべきか、マネージド型ハーネスに任せるべきかを判断したいチーム
