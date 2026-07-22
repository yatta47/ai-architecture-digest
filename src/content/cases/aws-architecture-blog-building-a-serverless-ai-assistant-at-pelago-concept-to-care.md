---
type: case
title: 依存症治療の医療機関がイベント駆動サーバーレスでAIアシスタントを2週間で構築
title_original: 'Building a serverless AI assistant at Pelago: concept to care in two weeks'
company: Pelago
industry: healthcare
cloud:
- aws
patterns:
- event-driven
- human-in-the-loop
- out-of-band-inference
- ai-agent
components:
- Amazon Bedrock
- AWS Lambda
- Amazon SNS
- Amazon DynamoDB
- Amazon RDS
- AWS AppSync
- Amazon API Gateway
outcome:
  type: speed
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/building-a-serverless-ai-assistant-at-pelago-concept-to-care-in-two-weeks/
published_at: '2026-07-22'
---

## 概要

依存症治療の digital clinic である Pelago は、ケアチームが会員との長期にわたる会話履歴を踏まえた返信案を得られるよう、Amazon Bedrock を使ったAIアシスタントをわずか2週間で構築した。メッセージ受信をSNSでファンアウトし、LLMによる提案生成を非同期のLambdaでバックグラウンド実行することで、コーチが画面を開いた際には事前生成済みの提案を100ミリ秒未満で表示できるようにした。PHIを扱う規制の厳しい環境でも、提案はすべて人間のコーチが確認・編集してから会員に届く設計になっている。

## 設計のポイント

- メッセージ受信とAI提案生成をSNSによるイベントファンアウトで分離し、新しい下流処理（AIアシスタント等)を既存コードの変更なしに追加できるようにする
- LLM推論を同期リクエストの外に置き、会話イベント受信時に非同期でバックグラウンド生成・保存しておくことで、コーチが会話を開いた際の表示は保存済みデータの参照のみで100ミリ秒未満に抑える
- 生成結果は自動送信せず必ず人間のケアチームが確認・編集してから会員に届く human-in-the-loop を徹底し、臨床上の安全性を担保する
- PHIを含むデータ処理をPelagoのAWS VPC境界内に閉じ、Lambda単位の疎結合構成により一部会員の処理失敗や急増が他の処理に影響しないようにする

## 使いどころ

- 長期にわたる会話履歴を踏まえた返信をケアチームや相談員が素早く作成したいヘルスケア/カウンセリング系サービス
- PHIなど機微情報を扱うため生成AIの出力を必ず人間がレビューしてから利用者に届ける必要がある規制業界
- LLM推論の待ち時間がユーザー体験を損なうため、事前生成・非同期処理でレイテンシを隠したいカスタマーサポート系アプリケーション
- 短期間でAI機能をプロトタイプから本番導入まで持っていく必要があるスタートアップ的な開発チーム
