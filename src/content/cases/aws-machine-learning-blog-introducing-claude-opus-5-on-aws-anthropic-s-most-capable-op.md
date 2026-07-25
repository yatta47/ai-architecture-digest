---
type: announcement
title: Claude Opus 5がAmazon Bedrock/Claude Platform on AWSで利用可能に
title_original: 'Introducing Claude Opus 5 on AWS: Anthropic''s most capable Opus model'
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- inference-optimization
- confidential-computing
components:
- Amazon Bedrock
- Claude Platform on AWS
- Claude Opus 5
- AWS CLI
- Boto3
- Anthropic SDK
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-claude-opus-5-on-aws-anthropics-most-capable-opus-model/
published_at: '2026-07-24'
---

## 概要

AnthropicのClaude Opus 5がAmazon BedrockとClaude Platform on AWSで提供開始され、エージェント型コーディングや長時間タスク、視覚理解などでOpus 5世代として初の性能向上をOpus級の価格で実現する。Bedrock上ではデフォルトでゼロデータ保持(ZDR)が有効になり、次世代推論エンジンによりAWS環境内でエンタープライズのセキュリティとリージョンデータレジデンシーを維持したまま利用できる。

## 設計のポイント

- Bedrockのデフォルト設定でゼロデータ保持(ZDR)を有効にし、エンタープライズのデータガバナンスを損なわずに最先端モデルを提供する
- Invoke/Converse APIに加えBedrock Mantle経由のAnthropic Messages APIもサポートし、既存資産に応じて複数の統合経路を選べるようにする
- tool_addition/tool_removalコンテンツブロックにより会話途中でツール定義を追加・削除でき、毎回全ツール配列を再送する必要がない
- 高リスク領域では自動的にOpus 4.8にフォールバックする仕組みを設け、フォールバック発生をユーザーに通知しAPI側で設定可能にする

## 使いどころ

- AWS環境内でセキュリティ・リージョンデータレジデンシー要件を保ったまま最先端モデルを使いたいエンタープライズチーム
- 既存のBedrock Invoke/Converse API資産を活かしつつ最新モデルに切り替えたい開発者
- 金融サービスなどコンプライアンス要求の高い業界で長時間稼働するエージェントを本番運用したい場合
