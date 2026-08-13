---
type: guidance
title: Bedrockコストをユーザー単位でAthena/CUDOSダッシュボードから分析する（Part 2）
title_original: 'Part 2: Amazon Bedrock cost attribution with Amazon Athena and CUDOS'
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
- llm-gateway
components:
- Amazon Bedrock
- Amazon Athena
- AWS Cost and Usage Report (CUR)
- CUDOS
- Amazon S3
- Claude Code
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/part-2-amazon-bedrock-cost-attribution-with-amazon-athena-and-cudos/
published_at: '2026-08-12'
---

## 概要

Part 1で導入したIAMプリンシパル単位のBedrockコスト追跡機能を、Cost and Usage Report(CUR) 2.0とAmazon Athena、CUDOSダッシュボードで可視化・分析する方法を解説。呼び出し元のIAMロールやセッション名単位でモデル利用コストをSQLクエリで集計し、チームやプロジェクト単位のチャージバックを実現する。

## 設計のポイント

- CUR 2.0のcaller identity(IAMプリンシパル)アロケーションデータを有効化し、line_item_iam_principalカラムでリクエスト単位の呼び出し元を特定する
- AthenaのSQLクエリでIAMプリンシパルタグ（team/project等）ごとにコストを柔軟に集計し、BIツールやチャージバック処理と連携する
- CUDOSダッシュボードで組織構造に沿った可視化を、Athenaクエリより低い運用負荷で提供する

## 使いどころ

- Claude CodeやCodexなどBedrock経由の複数アプリ・チームの利用コストを個別に把握したいFinOpsチーム
- IAMプリンシパル単位でのチャージバックや異常利用の検知を行いたい運用チーム
