---
type: case
title: 証券トレーディングデスク向け自然言語トレードアシスタント
title_original: 'Building trade assistant: How Jefferies optimized front office trading operations with AI'
company: Jefferies
industry: financial-services
cloud:
- aws
patterns:
- text-to-sql
- ai-agent
- rag
- guardrails
components:
- Strands Agents
- Amazon Bedrock
- Amazon Bedrock Knowledge Bases
- Amazon Bedrock Guardrails
- Amazon Titan Embeddings
- Amazon EKS
- Anthropic Claude
- MCP
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-trade-assistant-how-jefferies-optimized-front-office-trading-operations-with-ai/
published_at: '2026-07-23'
---

## 概要

Jefferiesは、Strands AgentsとAmazon Bedrockを用いてトレーダーが自然言語でリアルタイムのトレードデータを分析できるエージェント型トレードアシスタントを構築した。MCPツールで複数データソースに接続し、Bedrock Knowledge BasesによるRAGでスキーマ情報を取得してSQLを生成、Bedrock GuardrailsでPIIフィルタリングや行レベルのアクセス制御を実現した。ITやSMEに頼らずトレーダー自身がデータドリブンな意思決定を行えるようになった。

## 設計のポイント

- Bedrock Knowledge Basesでスキーマ・テーブル関係をRAG検索し、正確なSQL生成のコンテキストとして利用する
- MCPツールで複数のデータソース(インメモリ、履歴DB、FIXメッセージ)を統一インターフェースで抽象化する
- Bedrock GuardrailsでPIIフィルタリングと行レベルのデータ権限制御を組み込み、金融コンプライアンス要件を満たす
- 会話ログを監査証跡として保存し、コンプライアンス要件に対応する

## 使いどころ

- 非エンジニアのトレーダーがコーディングなしでデータ分析を行いたい金融機関
- 複数の異種データソースを横断する自然言語→SQLアシスタントを構築したいチーム
- 機密性の高い金融データにアクセス制御・監査証跡を要するAIエージェント導入
