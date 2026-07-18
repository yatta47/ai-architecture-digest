---
type: case
title: AIエージェントに業務管理データを開放するリモートMCPサーバー（AWS上に構築）
title_original: How Smartsheet built a remote MCP server on AWS
company: Smartsheet
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- unified-runtime
- event-driven
- context-engineering
components:
- Model Context Protocol (MCP)
- AWS Fargate
- Amazon ECS
- Amazon Kinesis Data Streams
- Amazon Managed Service for Apache Flink
- Amazon S3
- Amazon Bedrock
- Amazon Neptune
- Databricks
- AWS WAF
- AWS Shield
- Application Load Balancer
- Amazon ECR
- Amazon OpenSearch Service
- Amazon CloudWatch
- OpenTelemetry
- Datadog
- PagerDuty
data_sources:
- プロジェクトデータ
- タスク
- シート
- ワークスペース
- 変更イベント
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-smartsheet-built-a-remote-mcp-server-on-aws/
published_at: '2026-07-17'
---

## 概要

エンタープライズ業務管理プラットフォームのSmartsheetが、AIクライアントに自社データと機能への構造化アクセスを与えるリモートMCPサーバーをAWS上に構築した。Claude DesktopやAmazon Quickといったアシスタントに加え、自律的に動く社内外のカスタムAIエージェントが同じシート上で人間と協働し、数週間かかっていた作業を数日〜数時間に短縮する。既存APIと中央インテリジェンス層の上にトークンコスト削減とハルシネーション抑制を狙ったAI最適化インターフェースを載せ、内部テレメトリで30億トークン超を節約した。

## 設計のポイント

社内のSmart Assistと外部AIクライアントを同一インフラ・同一ツール群で動かす『一度作れば全エージェントが恩恵を受ける』パリティ設計が核。ステートレスなFargate/ECSにトラフィック量と計算負荷を組み合わせたターゲット追跡型オートスケールを敷き、バースト的なエージェント負荷を吸収する。ガバナンスはツールフレームワークに組み込み、readOnlyHint/destructiveHintのMCPアノテーションと組織単位の段階的アクセス制御で破壊的操作の確認フローを自動化する。

## 使いどころ

- 既存SaaSの業務データを、AIエージェントから安全に読み書きさせたいチーム
- 社内AIと外部AIクライアントを共通基盤で運用したいエンタープライズ製品チーム
