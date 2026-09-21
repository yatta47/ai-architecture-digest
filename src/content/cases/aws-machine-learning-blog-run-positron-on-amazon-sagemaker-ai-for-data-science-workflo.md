---
type: guidance
title: Positron IDEをSageMaker AI上で動かすデータサイエンス統合環境
title_original: Run Positron on Amazon SageMaker AI for data science workflows
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- unified-runtime
components:
- Amazon SageMaker AI
- Amazon Bedrock
- Amazon Athena
- AWS Glue Data Catalog
- Amazon S3
- Amazon ECR
- Positron
- Posit Assistant
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/run-positron-on-amazon-sagemaker-ai-for-data-science-workflows/
published_at: '2026-09-21'
---

## 概要

PositがSageMaker AI上でPositron IDEを提供し、Space実行ロールを介してAthena/Glue Data Catalog/S3への認証情報管理不要なデータアクセスを実現する。AIコーディング支援のPosit AssistantはBedrockをモデルプロバイダに使えるため、ガバナンス下のデータ探索からR/Pythonでの特徴量検証・モデル学習、エンドポイントデプロイまでを1つの環境内で完結できる。

## 設計のポイント

- Positronの実行をSageMaker StudioのSpace実行ロールに紐づけることで、キーの発行・保管なしにIAM権限に沿ったAthena/Glue/S3アクセスを実現する
- Posit AssistantのモデルプロバイダをBedrockにすることで、AIコーディング支援の推論を自社AWSアカウント・リージョン内に閉じ、顧客データがモデル提供元に共有されないようにする
- RでのETL・特徴量検証とPythonでのモデル学習を同一Space内のマルチ言語セッションで橋渡しし、ツール間のデータ受け渡しを不要にする
- 共有Spaceで複数人が同じPositronアプリケーションを使えるようにし、独立プロジェクト用のSpaceと使い分けて並行作業と共同作業を両立する

## 使いどころ

- governed dataへのアクセス管理・R/Python混在の分析・モデルデプロイまでを別々のツールを行き来せず1つのIDEで完結させたいデータサイエンスチーム
- AIコーディング支援を使いたいが、モデル提供元へのデータ送信を避けたい規制の厳しい業界のチーム
- スケジュール学習用にSageMaker AI training planでコンピュートを事前予約しつつ、対話的な探索と本番相当のデプロイを同じ環境で行いたい場合
