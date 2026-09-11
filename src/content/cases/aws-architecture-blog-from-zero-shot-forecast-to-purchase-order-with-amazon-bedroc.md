---
type: guidance
title: 小売の需要予測から発注までをAIエージェントで自動化する参照アーキテクチャ
title_original: From zero-shot forecast to purchase order with Amazon Bedrock AgentCore
industry: retail
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- decision-execution
- cost-optimization
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock
- Amazon Chronos2
- Strands Agents SDK
- Amazon SageMaker Serverless Inference
- Amazon S3
outcome:
  type: cost
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/from-zero-shot-forecast-to-purchase-order-with-amazon-bedrock-agentcore/
published_at: '2026-09-11'
---

## 概要

時系列基盤モデルAmazon Chronos2によるゼロショット需要予測と、Strands Agents SDK/Bedrock AgentCore上の4つのLLMエージェントによる発注意思決定を組み合わせたアーキテクチャ。SKUごとのモデル学習が不要になり、50SKU・4週間の検証でWAPE 12.3%、月次推論コストを98%削減、SKUオンボーディングを数週間からCSVアップロード5分未満に短縮した。

## 設計のポイント

- 時系列基盤モデル(Chronos2)によるゼロショット予測でSKUごとのモデル学習を不要にする
- Supervisor/Preprocessing/Forecasting/Reportingの4エージェントに役割分担し、決定的ツール呼び出しで各判断を監査可能にする
- ビジネスルール(安全在庫・発注ロット等)をJSON設定として分離し、コード変更なしで追加・変更できるようにする
- Bedrock AgentCoreのGateway面を必要最小限(8ツール中1つ)に絞りセキュリティ面を縮小する

## 使いどころ

- SKU数が多い小売業で、SKUごとのモデル運用コストを削減したい場合
- 需要予測から発注意思決定までを一貫して自動化・監査可能にしたい場合
- プロモーションや価格変更のWhat-ifシナリオ比較を行いたい発注担当者
