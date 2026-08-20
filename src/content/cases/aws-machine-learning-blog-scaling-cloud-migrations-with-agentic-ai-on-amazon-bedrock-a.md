---
type: case
title: AWS Professional Servicesのマルチエージェントによるクラウド移行加速基盤
title_original: Scaling cloud migrations with agentic AI on Amazon Bedrock AgentCore
company: AWS Professional Services
industry: cross-industry
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- event-driven
components:
- Amazon Bedrock AgentCore
- Strands Agents SDK
- AgentCore Gateway
- AgentCore Identity
- AWS Database Migration Service
- AWS Transform
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/scaling-cloud-migrations-with-agentic-ai-on-amazon-bedrock-agentcore/
published_at: '2026-08-20'
---

## 概要

AWS Professional Servicesは、300以上のアプリケーションを対象とした大規模クラウド移行のボトルネック（手作業の調査・IaC作成・移行後の運用）を解消するため、Strands Agents SDKとAmazon Bedrock AgentCore上で動くマルチエージェントフレームワークを構築した。Intake/IaC/ガバナンス/SREの4エージェントが発見からデプロイ、運用監視までを分担し、IaC開発時間をアプリあたり3〜4週間から数分に短縮した。

## 設計のポイント

- Intake・IaC・ガバナンス・SREという役割別の専用エージェントに分割し、移行ライフサイクルの各フェーズを担当させる
- AgentCore Gatewayが各エージェントのMCPツール呼び出しをIAMベースで認可し、AgentCore Identityがスコープ付きロールで認証する
- AgentCore memoryにIntakeエージェントの発見結果を書き込み、IaCエージェントがそれを読んで手作業の引き継ぎなしにコード生成を開始する
- AWS DMSやAWS Transformなどのマネージドサービスと自作エージェントを組み合わせ、データベース移行やレガシーコード変換を補完する

## 使いどころ

- 数百アプリ規模でデータセンター退去期限が決まっている大規模クラウド移行プログラム
- インフラ調査・IaC作成・移行後監視を手作業で行っており、エンジニア工数がボトルネックになっている移行チーム
- 人間の意思決定権限を保持しつつ定型作業だけをエージェントに委譲したいガバナンス重視の組織
