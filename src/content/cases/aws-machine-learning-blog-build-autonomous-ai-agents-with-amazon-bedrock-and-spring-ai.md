---
type: guidance
title: Spring AIとAgentCoreでJavaチームが自律エージェントを本番運用する
title_original: Build autonomous AI agents with Amazon Bedrock and Spring AI
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- document-processing
components:
- Amazon Bedrock
- Amazon Bedrock AgentCore
- Spring AI
- spring-ai-agentcore
- Terraform
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-autonomous-ai-agents-with-amazon-bedrock-and-spring-ai/
published_at: '2026-11-12'
---

## 概要

Spring AIとspring-ai-agentcoreを使い、JavaでBedrock AgentCore上に自律エージェントを構築する方法を示す。ツール呼び出しとメモリを持つ単一エージェントの旅行アシスタントと、専門エージェント・ルールエンジン・通知を組む文書処理のマルチエージェントを例にする。

## 設計のポイント

- Spring標準の自動構成・DI・Advisorでエージェントを組み、既存JVM運用資産を活かす。
- AgentCoreのランタイム・メモリ・IDを使い、スケールとガバナンスを任せる。
- 専門エージェントとルールエンジンを併用し、判断の一部を決定的にする。

## 使いどころ

- 既存Javaスタックで生成AIエージェントを本番化したいチーム。
- 請求書等の文書処理を多段エージェントで自動化したい企業。
- Terraformで環境を再現したい基盤担当。
