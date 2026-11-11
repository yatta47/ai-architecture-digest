---
type: guidance
title: AgentCore Evaluationsで業務成果から逆算するエージェント評価
title_original: 'The agent evaluation playbook: Built-in, DeepEval, and AutoEval on Amazon Bedrock AgentCore Evaluations'
industry: cross-industry
cloud:
- aws
patterns:
- eval
- llmops
- ai-agent
components:
- Amazon Bedrock AgentCore Evaluations
- DeepEval
- AutoEval
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/the-agent-evaluation-playbook-built-in-deepeval-and-autoeval-on-agentcore/
published_at: '2026-11-10'
---

## 概要

指標名から選ぶのではなく、業務上の成功を定義し、観測可能な振る舞いに分解して評価器へ対応付ける手順を示す。AgentCoreの組込み評価器とDeepEval、AutoEvalを使い、トレース単位とセッション単位で測る。

## 設計のポイント

- 成功を業務用語で定義し、観測可能な振る舞いに分ける。
- トレースレベルとセッションレベルの指標を使い分ける。
- 完了率が高くてもPII漏えいなど別観点の失敗が隠れる点に備える。

## 使いどころ

- 本番エージェントが業務に効いているか確認したいチーム。
- 評価指標の選定が曖昧になっている開発。
