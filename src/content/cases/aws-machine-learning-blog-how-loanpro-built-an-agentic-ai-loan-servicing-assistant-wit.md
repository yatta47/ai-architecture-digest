---
type: case
title: Bedrock AgentCoreによるローン窓口担当者向けマルチエージェント支援
title_original: How LoanPro built an agentic AI loan servicing assistant with Amazon Bedrock AgentCore
company: LoanPro
industry: financial-services
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- context-engineering
components:
- Amazon Bedrock
- Amazon Bedrock AgentCore
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-loanpro-built-an-agentic-ai-loan-servicing-assistant-with-amazon-bedrock-agentcore/
published_at: '2026-11-17'
---

## 概要

LoanProは、借り手からの通話対応中に担当者が口座情報・支払履歴・チケットを集める負担を減らすため、Bedrock AgentCore上でマルチエージェントの支援アシスタントを構築した。借り手の文脈を統合して次の行動を提案し、通話時間を最大15%短縮したとされる。

## 設計のポイント

- 散在する口座データ・履歴・チケットを集約して要約する文脈合成を専用エージェントに担わせている。
- エージェント実行基盤にマネージドなAgentCoreを使い、運用負荷を抑えている。
- 単なる要約でなく次アクションの推奨まで出し、通話中の判断を支援する。

## 使いどころ

- コールセンターなど、対応中に複数システムを参照する窓口業務。
- 金融・与信など、顧客文脈の把握に時間がかかる業務。
