---
type: guidance
title: MCPアプリでAIエージェントの可観測性検証をチャット内に統合
title_original: Agentic observability with Amazon OpenSearch Service MCP Apps
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- root-cause-analysis
- context-engineering
components:
- Amazon OpenSearch Service
- OpenSearch UI
- Amazon CloudWatch
- Amazon Managed Service for Prometheus
- MCP
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/agentic-observability-with-amazon-opensearch-service-mcp-apps/
published_at: '2026-08-25'
---

## 概要

Amazon OpenSearch Service の MCP Apps は、MCP のツール呼び出し結果をテキスト要約とインタラクティブな可視化（トレース、サービスマップなど）の二重レスポンスとして返し、AIエージェントによる根本原因分析の検証を同じチャット画面内で完結させる。ローカルMCPサーバーが仲介し、認証済みでOpenSearch UI経由の実データをレンダリングするため結果は決定的で、ブラウザへのタブ切り替えを排除できる。

## 設計のポイント

- MCPのレスポンスをテキストとビジュアルの二重チャネルに拡張し、エージェントの推論とユーザーの目視検証を同じスレッドで両立させる
- 可視化はAIの解釈ではなく実データに対するサーバーサイドのクエリ実行結果とすることで、決定論的で信頼できる検証を担保する
- MCPサーバーをローカル実行にしてAWSアカウント内の認証情報・データを外に出さない設計にする

## 使いどころ

- SREやオンコール担当者がエージェントの根本原因仮説を即座に目視検証したい場面
- ローカルでエージェント基盤を運用しつつ、ベンダー統合並みの検証体験がほしいチーム
