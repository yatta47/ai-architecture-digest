---
type: case
title: 医療記録の保険金請求審査を高速化するIDP×ドメイン特化LLM基盤
title_original: 'Reducing medical claims review time with AI on AWS: The EXL Medical IDP solution'
company: EXL
industry: healthcare
cloud:
- aws
patterns:
- document-processing
- fine-tuning
- multi-model-routing
- ai-agent
components:
- Amazon SageMaker AI
- Amazon Bedrock
- Amazon Textract
- AWS Step Functions
- Amazon API Gateway
- Amazon Cognito
- AWS Lambda
- Amazon DynamoDB
- Amazon RDS
- Amazon CloudWatch
- Amazon S3
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/reducing-medical-claims-review-time-with-ai-on-aws-the-exl-medical-idp-solution/
published_at: '2026-09-21'
---

## 概要

EXLは保険金請求審査で1件あたり100分超かかる医療記録レビューを自動化するため、テンプレート不要のIDPアプリXtrakto.AIと、保険・医療ドメインにファインチューニングしたEXL Insurance LLMを組み合わせた。SageMaker AIでドメイン特化LLMを学習・リアルタイム推論し、Bedrockの汎用基盤モデルを補完的に使い分けることで、抽出から要約・自然言語質問応答までを11ステップのパイプラインで完結する。

## 設計のポイント

- 汎用LLMのプロンプトだけに頼らず、保険・医療特有の専門用語やICD/CPTコード、傷病-治療関係を理解させるためドメインデータでLLMをファインチューニングする
- ドメイン特化のEXL Insurance LLMと汎用基盤モデル(Bedrock)をタスクごとに使い分け、追加インフラを持たずに適切なモデルへルーティングする
- SageMaker AI上でモデル学習・検証用の隔離環境と本番推論エンドポイントを分離し、継続的な改善が本番のクレーム処理に影響しないようにする
- Step Functionsでルーティングと抽出ワークフローを統合し、Textract/OCRによる前処理からLLMによる要約・照会・出力生成までを1つのオーケストレーションで扱う

## 使いどころ

- 数百ページに及ぶ非構造化の医療記録を、査定者・引受担当者が人手で読み込む前に要約・構造化したい保険会社
- 汎用LLMではカバーしきれないドメイン専門用語や規制対応が必要な、医療・保険領域のドキュメント処理
- 同一AWS環境でモデル開発から本番推論までを一貫させ、PHIなど機微情報の管理境界をIAMで統一したい場合
