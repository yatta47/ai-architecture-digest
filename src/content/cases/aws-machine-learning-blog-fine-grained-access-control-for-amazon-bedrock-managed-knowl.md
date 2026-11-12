---
type: guidance
title: LLMにユーザーを決めさせないエージェント検索のきめ細かいアクセス制御
title_original: Fine-grained access control for Amazon Bedrock Managed Knowledge Base tools
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- rag
- multi-tenant-rag
- guardrails
- ai-agent
components:
- Amazon Bedrock Managed Knowledge Base
- Amazon Bedrock AgentCore Gateway
- MCP
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/fine-grained-access-control-for-amazon-bedrock-managed-knowledge-base-tools/
published_at: '2026-11-12'
---

## 概要

全社共通のエージェントとKBで、各ユーザーが閲覧権限のある文書だけを検索できるようにする設計を示す。「誰として検索するか」をLLMの引数にせず、ゲートウェイ側でユーザー識別を渡すことでプロンプトインジェクションによる越権を防ぐ。

## 設計のポイント

- 検索ツールの引数に「誰として」を含めず、認証済みユーザーID等をインフラ側で注入する。
- KBのACL認識と組み合わせ、検索結果をユーザー権限で絞り込む。
- MCPツールをAgentCore Gateway経由で公開し認可を一元化する。

## 使いどころ

- 部門間で機密情報が混ざってはならない社内アシスタント。
- 複数顧客が1つのKBを共有するマルチテナントSaaS。
- プロンプトインジェクション耐性を求めるエージェント基盤。
