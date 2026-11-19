---
type: guidance
title: Bedrock AgentCore上のエージェントにツール障害を注入して耐障害性を検証
title_original: Resilience testing your agents on Amazon Bedrock AgentCore
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- chaos-engineering
- ai-agent
components:
- Amazon Bedrock AgentCore
- AWS Fault Injection Service
- AWS Systems Manager
- Strands Agents
- AWS Parameter Store
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/resilience-testing-your-agents-on-amazon-bedrock-agentcore/
published_at: '2026-11-18'
---

## 概要

AWS FISとSSM Automationで、Strandsエージェントのツール呼び出しに失敗や不正データを注入し、エージェントの挙動を検証する方法を示す。安全な失敗と無言の失敗を見分ける観測も用意する。

## 設計のポイント

- 測定可能な耐障害性の仮説を立ててから障害を注入する。
- 注入をエージェント内のツール呼び出しの前後で行い、再デプロイなしに切り替える。
- 安全な失敗と無言の失敗を区別できる観測を作る。

## 使いどころ

- 本番投入前のエージェントの障害時挙動を確認したいチーム。
- ツールの返す不正データへの耐性を試すとき。
