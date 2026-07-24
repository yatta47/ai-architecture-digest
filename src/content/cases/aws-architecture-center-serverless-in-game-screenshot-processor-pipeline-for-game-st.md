---
type: guidance
title: ゲーム内スクリーンショットをAIモデレーションするサーバーレスパイプライン
title_original: Serverless In-Game Screenshot Processor Pipeline for Game Studios
industry: media
cloud:
- aws
patterns:
- event-driven
- content-moderation
components:
- Amazon API Gateway
- AWS Lambda
- Amazon Rekognition
- Amazon S3
- Amazon DynamoDB
- Amazon CloudFront
- Amazon Cognito
- Amazon SNS
outcome:
  type: risk-compliance
source_id: aws-architecture-center
source_name: AWS Architecture Center
source_url: https://docs.aws.amazon.com/architecture-diagrams/latest/serverless-in-game-screenshot-processor-pipeline-game-studios/serverless-in-game-screenshot-processor-pipeline-game-studios.html?did=wp_card&trk=wp_card
published_at: '2021-12-24'
---

## 概要

プレイヤーがゲーム内で撮影したスクリーンショットをAPI Gateway経由でアップロードし、Lambda関数がAmazon RekognitionのDetectModerationLabelsで不適切表現を検出したうえで画像変換・透かし処理を行い、S3・DynamoDB・CloudFrontを組み合わせてギャラリー配信するサーバーレスのリファレンスアーキテクチャ。

## 設計のポイント

- アップロード直後にML APIでモデレーションを行い不適切画像の流通を未然に防ぐ
- メタデータをDynamoDBに、画像本体をS3に分離して保存しCloudFrontで配信する
- DynamoDB Acceleratorをオプションで挟み読み取りリクエストをキャッシュして高速化する

## 使いどころ

- ユーザー生成コンテンツを扱うゲームでの不適切画像の自動検閲
- スクリーンショット共有ギャラリー機能を持つゲームコミュニティサイト
