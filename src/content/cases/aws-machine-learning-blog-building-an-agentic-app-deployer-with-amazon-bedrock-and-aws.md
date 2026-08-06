---
type: case
title: 『意図を話すだけでアプリが出る』PDI Brewのエージェント型内製ツール自動プロビジョニング
title_original: Building an agentic app deployer with Amazon Bedrock and AWS Lambda
company: PDI Technologies
industry: retail
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- llm-gateway
components:
- Amazon Bedrock
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon S3
- Amazon CloudFront
- Microsoft Entra ID
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-an-agentic-app-deployer-with-amazon-bedrock-and-aws-lambda/
published_at: '2026-08-06'
---

## 概要

PDI Technologiesは、非技術者が自然言語で欲しいツールを説明するだけでSSO保護済みのマルチテナントWebアプリが自動生成される『PDI Brew』を構築した。意図を構造化マニフェストに変換するプランニングエージェントと、そのマニフェストからAWSリソース一式を決定的にオーケストレーションするプロビジョニングエージェントを分離し、後者にはガバナンス済みのAmazon Bedrockゲートウェイ経由でのみAI機能を組み込める設計にした。

## 設計のポイント

- 『意図を捉える』プランニングエージェントと『決定的に実行する』プロビジョニングエージェントを、信頼レベルの異なる2つのエージェントとして明確に分離する
- 両方のプランナー経路（既存AIアシスタントのスキル版とAWS境界内のBedrock版）が同一のマニフェストJSONを出力する契約にし、下流のプロビジョニング処理を経路によらず共通化する
- プロビジョニングのような『再現性・監査可能性・ハルシネーション排除』が必須の処理は、チャットセッションではなくLambda上の決定的なツール実行エージェントとして実装する
- 全アプリが同一プラットフォームを継承する設計にすることで、SSO・スコープ付きIAM・HTTPS・一元的な可観測性を『抜け道のない』デフォルトにする

## 使いどころ

- 優先度が低くバックログに積まれがちな『ロングテールの小規模内製ツール』の量産に悩む企業のプラットフォームチームとして
- 非エンジニアが自分で業務ツールを作れるようにしつつ、AI機能の利用だけはガバナンス・監査対象にしたい場合として
- サーバーレスでスケールtoゼロなマルチテナント基盤を、数百規模の小規模アプリ運用に適用したいケースとして
