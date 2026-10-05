---
type: guidance
title: AgentCore Evaluationsでマルチエージェントの説明可能性と有用性を評価する
title_original: Evaluating multi-agent systems for explainability and helpfulness with Amazon Bedrock AgentCore
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- eval
- multi-agent-orchestration
- guardrails
components:
- Amazon Bedrock AgentCore
- AgentCore Evaluations
- Amazon Bedrock Guardrails
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/evaluating-multi-agent-systems-for-explainability-and-helpfulness-with-amazon-bedrock-agentcore/
published_at: '2026-10-05'
---

## 概要

本番移行するマルチエージェントでは、回答品質だけでなくツール選択や制約順守、判断理由の説明が重要になる。AgentCore Evaluationsの組み込み評価器とカスタム評価器で、説明可能性を評価軸として運用する方法を示す。

## 設計のポイント

- 有用性・タスク成功・指示順守は組み込み評価器でベースライン化し、業務固有の検証はカスタム評価器で補う。
- 判断根拠の明示、根拠データの参照、コスト対サービスレベルなどのトレードオフ説明を評価項目にする。
- 実行後の評価と実行中のGuardrailsを組み合わせ、品質と安全を二層で担保する。

## 使いどころ

- サプライチェーンや金融分析などでエージェントを本番運用するチーム。
- 判断理由の説明責任が求められる業務のAI品質保証担当。
