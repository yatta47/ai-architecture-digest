---
type: announcement
title: SageMaker Python SDKからノートブック内で推論構成のベンチマーク・推奨・デプロイまで完結
title_original: LLM optimization integration for Amazon SageMaker Python SDK
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- cost-optimization
components:
- Amazon SageMaker Python SDK
- Amazon SageMaker AI
- Amazon SageMaker JumpStart
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/llm-optimization-integration-for-amazon-sagemaker-python-sdk/
published_at: '2026-08-06'
---

## 概要

Amazon SageMaker Python SDK v3に生成AI推論レコメンデーション機能が統合され、エンドポイントのベンチマーク、コスト対性能で順位付けされたデプロイ構成の生成、上位構成の実デプロイまでをノートブックから一気通貫で実行できるようになった。従来はコンソールやBoto3 APIの個別呼び出しが必要だった作業がSDKの数行で完結する。

## 設計のポイント

- インスタンスタイプやフレームワーク構成の総当たり検証を、実際のワークロードプロファイル（同時実行数・入出力トークン長など）に対する負荷試験として自動化する
- レコメンデーションをコスト対性能のトレードオフでランク付けし、推論フレームワーク（LMI/vLLM）の比較まで同一ワークフローに含める
- ModelBuilder.from_recommendation_jobで推奨ジョブを別プロセス・別セッションから再利用できるようにし、探索とデプロイの実行主体を分離できるようにする

## 使いどころ

- 生成AIモデルを本番投入する前に、インスタンスタイプやサービングスタックを手作業の試行錯誤なしに選定したいMLエンジニアとして
- TTFTやスループットなど複数の性能指標を天秤にかけながらコストを最適化したいプラットフォームチームとして
- 既存のノートブック・パイプライン運用にモデル最適化ワークフローをそのまま組み込みたい場合として
