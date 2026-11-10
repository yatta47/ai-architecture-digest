---
type: guidance
title: Amazon Bedrock呼び出しログを集約するトークン観測データレイク
title_original: Amazon Bedrock tokenomics data lake
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- cost-optimization
components:
- Amazon Bedrock
- Amazon CloudWatch
- Amazon Data Firehose
- Amazon S3
- Amazon Athena
- AWS CloudFormation
- AWS Lambda
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-tokenomics-data-lake/
published_at: '2026-11-10'
---

## 概要

複数アカウントのBedrock呼び出しログをCloudWatchのサブスクリプションフィルタで中央アカウントに集め、Firehose経由でAthenaから横断クエリできるデータレイクを構築する方法を示す。プロンプト、応答、トークン数、モデル、停止理由を呼び出し単位で分析し、コストを算出できる。CloudFormation 2本でIaC展開できる。

## 設計のポイント

- 各アカウントの呼び出しログを中央アカウントへ集約し、組織横断で単一テーブルとして扱う。
- プロンプト、応答、入出力トークン数、モデル、stop reasonを平坦化して保持し、無駄なプロンプトやトークン急増を調査可能にする。
- CloudFormationテンプレートで全アカウントに再現性高く展開する。

## 使いどころ

- 複数チームでBedrockを使うプラットフォーム/ML担当のコスト配賦
- トークン消費の急増やmax_tokensによる切断の原因調査
- プロンプト品質の監査と改善
