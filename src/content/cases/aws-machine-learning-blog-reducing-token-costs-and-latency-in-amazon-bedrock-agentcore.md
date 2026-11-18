---
type: case
title: FlightscapeがJSON大容量ペイロード向けにエージェントのトークンとレイテンシを削減
title_original: Reducing token costs and latency in Amazon Bedrock AgentCore JSON workloads
company: Flightscape
industry: logistics
cloud:
- aws
patterns:
- ai-agent
- context-engineering
- cost-optimization
components:
- Amazon Bedrock AgentCore
- LangGraph
- Amazon Bedrock Guardrails
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/reducing-token-costs-and-latency-in-amazon-bedrock-agentcore-json-workloads/
published_at: '2026-11-17'
---

## 概要

航空運用基盤Flightscapeは、20MB超のJSONを扱う研修スケジュール最適化エージェントで、ツール呼び出しごとに全ペイロードがコンテキストへ注入される問題を3つの組合せ戦略で解消した。23MBの代表ペイロードでトークンを最大71%、平均レイテンシを最大80%削減した。

## 設計のポイント

- 巨大ペイロードをそのままコンテキストに入れず、必要部分のみ参照する設計にする。
- 3つの戦略を組み合わせ可能にして段階的に適用する。
- LangGraphをAgentCore上で運用し、Guardrailsで応答を検証する。

## 使いどころ

- 数十のツールと巨大な構造化データを扱う業務エージェント。
- マルチターンでコンテキスト圧迫に悩むチーム。
