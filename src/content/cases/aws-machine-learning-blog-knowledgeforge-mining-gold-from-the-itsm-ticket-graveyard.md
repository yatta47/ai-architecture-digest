---
type: case
title: KnowledgeForge：解決済みITSMチケットからナレッジベースを自動生成・浄化する仕組み
title_original: 'KnowledgeForge: mining gold from the ITSM ticket graveyard'
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- document-processing
- rag
- human-in-the-loop
components:
- Amazon Bedrock
- Amazon S3 Vectors
- AWS Step Functions
- Amazon ECS
- AWS Fargate
- Amazon DynamoDB
- Amazon SQS
- Amazon Bedrock Guardrails
- Anthropic Claude Sonnet 4.5
- Amazon Titan Text Embeddings V2
- ServiceNow
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/knowledgeforge-mining-gold-from-the-itsm-ticket-graveyard/
published_at: '2026-08-19'
---

## 概要

解決済みのITサポートチケットに眠る知見をナレッジベース記事として掘り起こし、同時に既存記事の重複・陳腐化・品質のばらつきを整理するKnowledgeForgeのアーキテクチャ。クラスタ化したチケット群からAmazon Bedrock（Claude Sonnet 4.5）で記事案と根本原因分析文書を生成し、Amazon S3 Vectorsで重複検出、AWS Step FunctionsでClassify/Dedup/Score/Improveの4段階キュレーションを回し、最終的にServiceNow上のナレッジマネージャーがレビュー承認するクローズドループを構築する。

## 設計のポイント

- 生成とキュレーションを別サブシステムに分け、キュレーションが記事をベクトル化してS3 Vectorsインデックスに書き込み、次回の生成がそのベクトルをグラウンディングとして再利用するクローズドループにする
- 生成は数分かかりバースト的に大量発生する重い処理のため、キューの深さに応じてスケールするAmazon ECS on Fargateのコンテナで実行し、短時間実行向けのLambdaには向かないワークロード特性に合わせる
- 新規記事作成前に類似の既存記事上位5件を取得してモデルへ参照コンテキストとして渡すRAGで、用語の一貫性を保ち手順の捏造を減らす。参照記事が無い場合は生成結果を要レビューとフラグする
- 最終的な公開判断は必ず人間のナレッジマネージャーが担うワークフローとし、生成・キュレーションの自動化とヒューマンレビューを明確に分離する

## 使いどころ

- 解決済みチケットの知見がナレッジベースに反映されず、同じ問題を毎回一から調査しているサポート組織
- 重複記事や陳腐化した記事が積み重なり、検索してもどれが正しいか分からなくなっているナレッジベース運用
- 大規模なドキュメント生成パイプラインを生成AIで構築する際の、生成とキュレーションの責務分離パターンを探しているチーム
