---
type: guidance
title: API GatewayとDynamoDB Streamsで29秒制限を回避する非同期イベント処理パターン
title_original: Process events asynchronously with Amazon API Gateway and Amazon DynamoDB Streams
industry: cross-industry
cloud:
- aws
patterns:
- event-driven
- parallel-execution
components:
- Amazon API Gateway
- Amazon DynamoDB
- Amazon DynamoDB Streams
- AWS Lambda
- Amazon EventBridge
- Amazon SNS
- AWS CDK
data_sources:
- ジョブパラメータ
- イベント
- ジョブ結果
outcome:
  type: reliability
source_id: aws-architecture-center
source_name: AWS Architecture Center
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/processing-events-asynchronously-with-amazon-api-gateway-and-amazon-dynamodb-streams.html?did=pg_card&trk=pg_card
published_at: '2024-05-10'
---

## 概要

API Gatewayには29秒の統合タイムアウトというハード制限があり、同期処理を前提とするため長時間かかる非同期ワークロードには不向きである。本パターンはAPI Gateway・DynamoDB Streams・Lambdaを組み合わせ、POSTでジョブを受け付けてジョブIDを即返し、DynamoDBへの書き込みをトリガーにLambdaがStreams経由で非同期にイベントを処理する構成を示す。同一入力での並列ジョブ実行にも対応する。

## 設計のポイント

- 同期APIと非同期処理をDynamoDB Streamsで疎結合にし、POSTでジョブ登録・GETで結果取得のポーリング型インターフェースにすることで29秒制限を回避する
- 処理失敗時はイベントソースマッピングからSNSトピック経由でエラーハンドリングLambdaへ、さらに失敗すればEventBridgeアーカイブへ退避してリプレイ可能にする多段のエラー処理を備える
- 結果の整合性は楽観的ロックで担保する

## 使いどころ

- 29秒を超える長時間ジョブや重い計算をREST API経由で受け付けたい場面に有効
- クライアントを待たせたくないサーバーレス構成に向く
- Streams読み取りは2つまで、Lambda実行は15分までといった制約を許容できる場面に向く
