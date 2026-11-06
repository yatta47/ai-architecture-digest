---
type: announcement
title: 出典付き回答を1回のツール呼び出しで返すWeb Answer
title_original: Getting started with Web Answer on Amazon Bedrock AgentCore
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- rag
- parallel-execution
components:
- Amazon Bedrock AgentCore
- AgentCore Gateway
- Web Answer
- Strands Agents
- MCP
- AWS IAM
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/getting-started-with-web-answer-on-amazon-bedrock-agentcore/
published_at: '2026-11-05'
---

## 概要

Amazon Bedrock AgentCoreのWeb Answerが一般提供となった。検索、取得、要約、引用付与のパイプラインを自前で組まずに、自然言語の質問から出典付き回答をGateway経由のMCPツールとして得られる。

## 設計のポイント

- Gatewayにマネージドコネクタをターゲットとして追加するだけで、ツールスキーマと認証を任せられる。
- 検索を計画し並列実行し、証拠不足なら再検索するエージェント型検索を内部で担う。
- 生の検索結果が必要ならWeb Search、完成した回答が必要ならWeb Answerと使い分ける。

## 使いどころ

- 最新のWeb情報に基づく事実確認をエージェントの一部に組み込みたい場面。
- 自前の検索・要約・引用パイプラインの保守を減らしたい開発者。
