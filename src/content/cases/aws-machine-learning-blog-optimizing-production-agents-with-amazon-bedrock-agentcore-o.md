---
type: guidance
title: 本番AIエージェントの性能・メモリ問題をAgentCore Observabilityで診断する
title_original: Optimizing production agents with Amazon Bedrock AgentCore Observability
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- llmops
- root-cause-analysis
- memory-consolidation
components:
- Amazon Bedrock AgentCore
- Amazon CloudWatch
- AgentCore Observability
- AgentCore Evaluations
- AgentCore Insights
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/optimizing-production-agents-with-amazon-bedrock-agentcore-observability/
published_at: '2026-07-31'
---

## 概要

本番運用中のAIエージェントが正しく動作しつつも低速化・メモリ肥大化する問題を、AgentCore ObservabilityとCloudWatchのトレース/メトリクスクエリで診断する手法を解説。レイテンシのボトルネック特定からメモリ名前空間の分割まで、具体的な対処法を示す。

## 設計のポイント

- CloudWatchクエリで高レイテンシのリクエストを抽出し、RequestId単位でスパンのタイムラインを分析してボトルネックを特定する
- メモリは用途別の名前空間に分割し、サイズ上限を設けて古い会話は要約で圧縮する
- 独立したツール呼び出しは逐次実行ではなく並列実行にしてレイテンシを削減する
- プロンプトに簡潔な出力を促す制約を加えてトークン生成量とコストを抑える

## 使いどころ

- プロトタイプから本番移行後にレイテンシやコストが徐々に悪化するエージェントの運用担当者
- 顧客対応チャットボットなど低レイテンシが求められるインタラクティブ用途の性能改善
- 長時間セッションでメモリが肥大化するエージェントのメモリ設計見直し
