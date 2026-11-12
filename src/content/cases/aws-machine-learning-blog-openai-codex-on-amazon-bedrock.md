---
type: guidance
title: Codex等のコーディングエージェントをBedrockとIAM統制下で導入する方法
title_original: OpenAI Codex on Amazon Bedrock
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- llm-gateway
- guardrails
- policy-as-code
components:
- OpenAI Codex
- Amazon Bedrock
- AgentCore Gateway
- LiteLLM
- Portkey
- IAM
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/openai-codex-on-amazon-bedrock/
published_at: '2026-11-11'
---

## 概要

CodexをAmazon Bedrockの推論で使う際に、既存のIAM・リージョン・可観測性に乗せる方法を示す。最小権限のパイロットから始め、Native AWS Access、AgentCore Gateway、LLMゲートウェイの順に統制強度を選ぶ。

## 設計のポイント

- まず最小権限のネイティブAWSアクセスで小規模に試す。
- ルーティングやGuardrailsが要るときにAgentCore Gatewayを使う。
- リクエスト経路で統制したい場合はLLMゲートウェイを置く。

## 使いどころ

- 開発者向けAIツールを安全に展開したいプラットフォームチーム。
- モデルアクセスとIDを既存基盤に統合したい企業。
- 段階的にガバナンスを強めたい組織。
