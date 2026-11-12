---
type: guidance
title: A2Aで組織境界を越えるマルチエージェント連携のAWSリファレンス構成
title_original: Build composable, interoperable multi-agent systems with A2A on AWS
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
components:
- A2A
- LangChain
- Strands Agents
- Amazon Bedrock AgentCore
- OAuth 2.0
- OIDC
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-composable-interoperable-multi-agent-systems-with-a2a-on-aws/
published_at: '2026-11-12'
---

## 概要

別AWSアカウントにある企業側のLangChainオーケストレーターとISV側のStrands Agentsを、A2Aプロトコルで連携させるリファレンス構成を示す。相互にフレームワークやシークレットを共有せず、Agent Cardの登録でスキルを追加できる。

## 設計のポイント

- Agent Cardを登録するだけで新スキルを追加でき、既存エージェントを変更しない。
- OAuth 2.0/OIDCなど既存の認証標準で境界をまたぐ認可を行い、秘密情報を共有しない。
- フレームワーク非依存のプロトコルで、顧客ごとのカスタム連携コードを不要にする。

## 使いどころ

- 自社エージェントを顧客に提供するISV。
- 部門ごとに異なるフレームワークのエージェントを束ねる企業。
- パートナー向けにエージェントを公開したい組織。
