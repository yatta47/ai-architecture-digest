---
type: case
title: 銀行API統合オンボーディングを支援するマルチエージェントAIアシスタント
title_original: How Ninth Wave built AI-powered open finance onboarding on Amazon Bedrock
company: Ninth Wave
industry: financial-services
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- multi-tenant-rag
- defense-in-depth
components:
- Amazon Bedrock AgentCore
- Strands Agents
- Amazon OpenSearch Service
- Amazon S3
- Amazon CloudFront
- AWS WAF
- Amazon ECS
- AWS Fargate
- AWS Secrets Manager
- AWS IAM
- AWS KMS
- AWS CloudTrail
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-ninth-wave-built-ai-powered-open-finance-onboarding-on-amazon-bedrock/
published_at: '2026-09-14'
---

## 概要

Ninth WaveはオープンファイナンスAPIの銀行間統合を支援するAIアシスタント「Compass」をAmazon Bedrock AgentCore上に構築した。意図分類でリクエストを7つの専門エージェントへルーティングするマルチエージェント構成とし、金融機関向けの厳格なセキュリティ・コンプライアンス要件を満たしながらオンボーディング作業を自己サービス化した。

## 設計のポイント

- 単一のRAGエージェントではなくタスクごとに専門化した複数エージェントに分割し、コンテキストを汚さず精度を上げる
- オーケストレーターが意図分類を一度だけ行い適切な専門エージェントへルーティングする
- タスクの複雑さに応じて軽量モデルと高推論モデルを使い分ける per-task モデル選択
- エージェント呼び出し前にテナント固有のコンテキストのみを組み立て、テナント間のデータ混入を防ぐ

## 使いどころ

- 複数の外部パートナー（銀行・アグリゲーター）が同じプラットフォームを使う多テナントSaaSのAI化
- 規制業界で監査ログ・最小権限・暗号化などのコンプライアンス要件を保ちながらAIを導入したい場合
- API仕様の差異吸収やフィールドマッピングなど専門知識が要る定型作業の自己サービス化
