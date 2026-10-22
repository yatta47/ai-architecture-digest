---
type: case
title: Step FunctionsとAgentCoreで決定論的に回す医療用語コーディング自動化
title_original: Automate medical coding with Step Functions and Amazon Bedrock AgentCore
industry: healthcare
cloud:
- aws
patterns:
- ai-agent
- human-in-the-loop
- guardrails
- cost-optimization
components:
- AWS Step Functions
- Amazon Bedrock AgentCore
- Amazon Bedrock
- Amazon Aurora
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/automate-medical-coding-with-step-functions-and-amazon-bedrock-agentcore/
published_at: '2026-10-21'
---

## 概要

臨床の自由記述をMedDRAやWHODrugなどの標準コードに変換する作業を、Step Functionsでの決定論的な流れと、AgentCoreハーネスによる限定的なエージェント推論で自動化する構成。安全ブロックリスト、完全一致、AIエージェントの順にコストの低い手段から段階的に回し、曖昧なものだけ人の承認に回す。

## 設計のポイント

- 順序と承認ゲートはワークフローエンジンが持ち、エージェントは各ステップ内の判断だけを担う。
- 最も安く決定論的な手段から使い、確信が持てないときだけ上位の手段へ引き上げる。
- エージェントが決めるのはコードと確信度までで、次の遷移は決めさせない。ステートマシン定義から実行経路を監査できる。

## 使いどころ

- 安全性が重要で、監査と再現が求められる医療・治験データの処理。
- LLMを使いつつ実行経路を審査者が読める形に保ちたい規制業種。
