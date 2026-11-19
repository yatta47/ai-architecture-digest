---
type: case
title: SalesforceがSageMakerのリージョン横断推論ルーティングで容量を共有
title_original: How Salesforce is advancing global-scale model serving with cross-Region inference routing in Amazon SageMaker
  AI
company: Salesforce
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- llm-gateway
- disaster-recovery
components:
- Amazon SageMaker AI
- SageMaker cross-Region inference routing
- Internal Gateway
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-salesforce-is-advancing-global-scale-model-serving-with-cross-region-inference-routing-in-amazon-sagemaker-ai/
published_at: '2026-11-18'
---

## 概要

SalesforceのAgentforce Foundationチームは、30以上のリージョンでモデルを配信しており、リージョンごとの容量分断が可用性問題になっていた。SageMaker AIのリージョン横断ルーティングで複数リージョンとアカウントのエンドポイントを1つの呼び出し経路にし、データレジデンシーを保ったまま容量を足している。

## 設計のポイント

- 顧客ごとのピークが重なるため、リージョンごとに最大を確保せず容量を共有する。
- 既存エンドポイントを変えず、内部ゲートウェイからの単一経路にまとめる。
- データレジデンシーの約束を守る範囲でルーティングする。
- どのリクエストがどこで処理されたかを観測できる。

## 使いどころ

- 多リージョンでモデルを配信しているプラットフォーム事業者。
- トラフィックの急増を吸収したいとき。
