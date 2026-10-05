---
type: guidance
title: GovCloud上のBedrockでClaude Codeを使う規制ワークロード向け開発環境
title_original: Supercharge regulated workloads with Claude Code and Amazon Bedrock
company: AWS
industry: public-sector
cloud:
- aws
patterns:
- ai-agent
- guardrails
- defense-in-depth
components:
- Amazon Bedrock
- AWS GovCloud (US)
- Claude Code
- Claude Opus 5.5
- Claude Sonnet 5.5
- Amazon Bedrock Guardrails
- AWS IAM
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/supercharge-regulated-workloads-with-claude-code-and-amazon-bedrock/
published_at: '2026-10-05'
---

## 概要

AWS GovCloud (US)のAmazon BedrockでClaude Opus 5.5/Sonnet 5.5が使えるようになり、ITARなど規制要件のあるワークロードでもClaude Codeを使ったAI支援開発が可能になった。bedrock-runtimeとbedrock-mantleの2種類のエンドポイントの違いと、IAM権限・セットアップ手順を解説する。

## 設計のポイント

- 監査証跡やGuardrails、Knowledge Basesが必要なら bedrock-runtime、Messages API固有機能が必要なら bedrock-mantle と、要件でエンドポイントを使い分ける。
- IAMはエンドポイントごとに最小権限（InvokeModel系／bedrock-mantle系）を付与し、短期認証情報やSSOで接続する。
- 対話型ウィザードと環境変数による手動設定を用意し、個人利用と組織への配布展開の両方に対応する。

## 使いどころ

- ITARやFedRAMP/IL4・IL5が求められる政府系・防衛系の開発チーム。
- コンプライアンス境界の内側でコーディングエージェントを導入したい組織。
