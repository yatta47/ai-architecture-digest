---
type: guidance
title: ローコード自動化ツールn8nから本番グレードのエージェント基盤AgentCore harnessを呼び出す
title_original: Run production AI agents in n8n with Amazon Bedrock AgentCore harness
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- unified-runtime
- memory-consolidation
components:
- Amazon Bedrock AgentCore
- AgentCore harness
- n8n
- Strands Agents
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/run-production-ai-agents-in-n8n-with-amazon-bedrock-agentcore-harness/
published_at: '2026-08-05'
---

## 概要

n8nの標準AI Agentノードは単発のモデル呼び出しにとどまるのに対し、OSSコミュニティノード@aws/n8n-nodes-agentcoreはAmazon Bedrock AgentCore harnessの本番グレードのオーケストレーション（永続メモリ・分離実行環境・ツール・複数モデルプロバイダー切り替え）をn8nのビジュアルエディタからそのまま利用できるようにする。設定だけでエージェントを組み立て、必要に応じてStrands Agentsのコードにエクスポートして継続開発もできる。

## 設計のポイント

- モデル呼び出し自体と、その周りのオーケストレーションループ・ツール呼び出し・コンテキスト管理・セッション分離を分けて考え、後者を『harness』としてマネージドサービス化する
- Harness ARNを空にすればノードが初回実行時にエージェントを自動作成・以後は再利用・設定変更時は更新するという、コードを書かない運用者向けのライフサイクル管理にする
- Amazon Bedrock・OpenAI・Google Gemini・LiteLLM対応プロバイダーを同一ノードで扱えるようにし、会話の途中でもプロバイダーを切り替えられるようにする
- 設定で足りなくなった場合はハーネスをStrands Agentsのコードとしてエクスポートし、同じ実行基盤上でコードベースの開発に移行できる退路を用意する

## 使いどころ

- ノーコード/ローコードで業務を自動化しているチームが、単発モデル呼び出しを超えた本番グレードのエージェントを構築したい場合として
- セッションをまたいだ会話メモリやユーザースコープの記憶を、自前でインフラを組まずに持たせたい場合として
- VPC内で完結するプライベートなエージェント実行など、n8nのビジュアル開発とエンタープライズ要件を両立したい場合として
