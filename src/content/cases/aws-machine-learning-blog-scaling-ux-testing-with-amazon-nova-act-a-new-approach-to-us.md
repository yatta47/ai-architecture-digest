---
type: guidance
title: Amazon Nova Actによる大規模UXテスト自動化基盤
title_original: 'Scaling UX testing with Amazon Nova Act: A new approach to user flow analysis'
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- parallel-execution
- document-processing
- rag
components:
- Amazon Nova Act
- Amazon Bedrock Knowledge Base
- Claude 4.5 Sonnet
- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon ECS
- AWS Fargate
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/scaling-ux-testing-with-amazon-nova-act-a-new-approach-to-user-flow-analysis/
published_at: '2026-07-14'
---

## 概要

Amazon Nova Actの視覚的なブラウザ理解を活用し、サイトドキュメントからユーザーフローのテストシナリオを自動生成、並列ブラウザセッションで大規模にUXテストを実行し、摩擦ポイントを自動分析するクラウド型プラットフォームを解説。

## 設計のポイント

- サイトドキュメントをBedrock Knowledge Baseに取り込み、Claude 4.5 Sonnetでタスクからテスト手順を生成する。
- セレクタに依存する従来の自動化と異なり、Nova Actはスクリーンショットを視覚的に解釈するため画面変更に強い。
- DynamoDB Streamsをトリガーに生成されたフローをECS/Fargateで並列実行し、実行のたびに詳細な推論ログとスクリーンショットを保存する。

## 使いどころ

- 手動テストでは網羅できないエッジケースを大規模にカバーしたいプロダクトチーム。
- UI変更でスクリプトが頻繁に壊れる従来のUI自動化から脱却したいQA/UXリサーチチーム。
