---
type: case
title: AWS営業向けマルチエージェントを守る継続的評価ループ
title_original: 'Building trust in AI agents: A production-ready evaluation framework with Amazon Bedrock AgentCore'
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- eval
- llmops
- ci-cd
- multi-agent-orchestration
components:
- Amazon Bedrock AgentCore
- AgentCore Evaluations
- Amazon Bedrock Guardrails
- Amazon CloudWatch
- Amazon S3
- Amazon Redshift
- Amazon Quick
- AWS Lambda
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-trust-in-ai-agents-a-production-ready-evaluation-framework-with-amazon-bedrock-agentcore/
published_at: '2026-10-16'
---

## 概要

AWSのSMGS Operationsチームが、営業向けマルチエージェント（Performance/Customer/Data Insights）の品質を守るため、AgentCore Evaluationsを軸にした9段階の評価フレームワークを構築した事例。単価の桁違い表示のような「自信満々の誤答」は従来の稼働監視では検知できず、CI/CDゲート、カナリアスコア、ドリフト検知、フィードバックループで継続的に品質を測る。

## 設計のポイント

- レイテンシやエラー率だけでなく、回答の正確性・根拠性を評価対象にして、静かに誤る失敗を捉える。
- リリース前のCI/CDゲートと本番でのカナリアスコア・ドリフト検知を組み合わせ、データ・プロンプト・コードの変更を継続的に守る。
- データ・ツール・プロンプトの協調リリースがずれる不整合期間（合格率78%→38%）を想定し、失敗を原因レイヤーまで遡れるようにする。
- カスタム評価器をLambdaで実装し、結果をS3/Redshiftに永続化してダッシュボード化する。

## 使いどころ

- 複数サブエージェントを本番運用し、一部の劣化が全体に波及するリスクを抱えるチーム。
- 数値の正確さが業務判断に直結する社内BIや営業支援のエージェント。
- データ更新が定期的に走り、リリースなしでも品質が変動するエージェント基盤。
