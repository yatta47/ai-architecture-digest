---
type: guidance
title: AgentCore Evaluationsに決定モデルを組み込むスクリーニング評価
title_original: Use decision models with Amazon Bedrock AgentCore Evaluations
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- eval
- ai-agent
- guardrails
components:
- Amazon Bedrock AgentCore Evaluations
- AWS Lambda
- Strands Agents
- Strands Decider 2B
- Jev (TypeSafe)
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/use-decision-models-with-amazon-bedrock-agentcore-evaluations/
published_at: '2026-11-04'
---

## 概要

Amazon Bedrock AgentCore Evaluationsのコードベース評価器から、固定の選択肢に対し校正済み確率を返す決定モデル（Jev、Strands Decider 2B）を呼ぶ方法の解説。HRアシスタントを例に、LLM-as-a-judgeと併用してスクリーニング層にする。

## 設計のポイント

- Lambdaの評価器でAgentCoreの入力を決定モデルのリクエストに変換し、確率を評価結果に戻す。
- ポリシー遵守などの狭い二択・多択・段階評価を決定モデルに任せ、閾値判定できる確率を得る。
- 全ターンを決定モデルで絞り込み、要調査のターンだけ説明付きの組み込みLLM評価器で深掘りする。

## 使いどころ

- エージェントの本番トラフィックを低コストで継続評価したい運用担当
- 安全性・トピック逸脱などのルーブリックを一貫して適用したいチーム
