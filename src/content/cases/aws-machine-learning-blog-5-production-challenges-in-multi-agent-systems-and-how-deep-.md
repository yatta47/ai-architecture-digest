---
type: case
title: マルチエージェント本番運用の5課題とDeep Insightの解決策
title_original: 5 production challenges in multi-agent systems and how Deep Insight solved them
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- multi-agent-orchestration
- context-engineering
- human-in-the-loop
- ai-agent
components:
- Strands Agents SDK
- Amazon Bedrock
- Amazon Bedrock AgentCore
- Application Load Balancer
- AWS Fargate
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/5-production-challenges-in-multi-agent-systems-and-how-deep-insight-solved-them/
published_at: '2026-10-21'
---

## 概要

AWSのソリューションアーキテクトチームが作った本番向けマルチエージェントシステムDeep Insightの連載第1回。CSVと自然言語の指示から、Coordinator・Planner・Supervisor・Coder・Validator・Reporter・Trackerが連携して分析とレポートを生成する。本番運用で直面する5つの課題への対処を整理する。

## 設計のポイント

- プロンプトだけに頼らず、エージェントがいつ検証し失敗時にどうするかまで認知アーキテクチャと実行フローとして設計する。
- 分析計画をユーザーに提示して承認を得てから実行するHuman-in-the-Loopを入れる。
- 役割を分けた階層構造にして、検証担当を実行担当と分離する。

## 使いどころ

- PoCは動くが本番でビジネスロジックの遵守や検証の抜けに悩むエージェント開発チーム。
- データ分析からレポート作成までを自動化したい企業。
