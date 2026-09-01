---
type: case
title: 統合ワークフローのXMLをDAG化しBedrock/Claudeで自動ドキュメント生成するBoomi Scribe
title_original: How Boomi Scribe streamlines documentation using AWS
company: Boomi
industry: other
cloud:
- aws
patterns:
- document-processing
- ai-agent
- context-engineering
components:
- Amazon Bedrock
- Anthropic Claude Haiku 4.5
- Amazon SageMaker AI
- Amazon S3
- Amazon DynamoDB
- AWS Lambda
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-boomi-scribe-streamlines-documentation-using-aws/
published_at: '2026-09-01'
---

## 概要

Boomiは、統合プロセスの複雑なXML定義をDAG(dot記法)へ変換し、Amazon BedrockのClaude Haiku 4.5に渡してドキュメントを自動生成・バージョン間差分比較するAIエージェント「Boomi Scribe」を構築した。33,000社超の顧客が使う統合プラットフォーム上で、手作業だったドキュメント作成・保守の技術的負債を解消する。

## 設計のポイント

- XMLの複雑な生表現をそのままモデルに渡さず、DAGのdot記法という構造化中間表現に変換してからLLMに入力する
- few-shot学習が可能な小型モデル(Claude Haiku)を採用し、大量顧客規模でのコストとレイテンシを両立する
- バージョン間のDAG差分比較を組み込み、ドキュメント生成だけでなく変更点のハイライトも自動化する
- Lambdaでパース〜生成〜比較〜保存のパイプライン全体をオーケストレーションし、S3/DynamoDBに結果とメタデータを永続化する

## 使いどころ

- 複雑な自動化ワークフローの保守ドキュメントが属人化・陳腐化しがちなiPaaS/ETL製品チーム
- 監査やコンプライアンスのためにプロセス変更履歴の説明可能性を高めたい組織
- 構造化データ(グラフ/DAG)を中間表現としてLLMに渡す設計を検討しているエンジニア
