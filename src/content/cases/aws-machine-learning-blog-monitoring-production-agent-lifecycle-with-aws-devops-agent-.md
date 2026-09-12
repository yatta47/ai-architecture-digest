---
type: case
title: 航空予約マルチエージェントシステムの品質×インフラ二層監視
title_original: Monitoring production agent lifecycle with AWS DevOps Agent and AgentCore Evaluations
industry: logistics
cloud:
- aws
patterns:
- multi-agent-orchestration
- eval
- root-cause-analysis
- llmops
components:
- Amazon Bedrock AgentCore
- AgentCore Evaluations
- AWS DevOps Agent
- Amazon CloudWatch
- Strands Agents
- OpenTelemetry
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/monitoring-production-agent-lifecycle-with-aws-devops-agent-and-agentcore-evaluations/
published_at: '2026-09-11'
---

## 概要

AWSは航空予約システムを題材に、4つの専門エージェントで構成されるマルチエージェント本番運用の監視アーキテクチャを提示する。Amazon Bedrock AgentCore Evaluationsによる継続的な品質スコアリングと、AWS DevOps Agentによる自律的なインフラ障害調査を組み合わせ、インフラは正常なのにエージェントの応答品質が劣化するといった従来の監視では見えない障害を検知する。

## 設計のポイント

- インフラ監視（CloudWatchメトリクス）とエージェント品質監視（LLM-as-a-Judgeによる有用性・正答性・タスク達成度の評価）を別レイヤーとして両立させる
- 品質スコアが低下したセッション群にパターン分析をかけ、誤ったツール選択などの共通原因からプロンプトやオーケストレーションの改善案を自動生成する
- インシデント発生時はDevOpsエージェントがIAM権限・呼び出しログ・オーケストレーショントレースを横断して根本原因まで自動追跡する

## 使いどころ

- Swarmパターンなど実行グラフが固定されないマルチエージェント構成で、ハンドオフ地点の障害を可視化したいチーム
- エラーは出ていないのに顧客体験が悪化しているサイレント障害を早期検知したい本番運用チーム
