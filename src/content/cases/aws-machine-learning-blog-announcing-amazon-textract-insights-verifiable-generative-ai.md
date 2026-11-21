---
type: announcement
title: 自然言語でスキーマを定義して文書を抽出するAmazon Textract Insights
title_original: 'Announcing Amazon Textract Insights: Verifiable generative AI for documents'
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- document-processing
components:
- Amazon Textract
- Amazon S3
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/announcing-amazon-textract-insights-verifiable-generative-ai-for-documents/
published_at: '2026-11-20'
---

## 概要

Amazon Textract Insightsが一般提供となった。自然言語で説明したフィールドを持つブループリントで、最大3,000ページの混在書類パケットから、信頼度とページ根拠付きの構造化結果を1つの非同期APIで得られる。

## 設計のポイント

- JSON Schemaのブループリントで項目を定義し、原文そのままの読み取りか推論かを項目ごとに指定する。
- 全値に信頼度スコアとページ単位の根拠を付け、自動受理と人手確認を分けられるようにする。
- 分割、分類、抽出を単一のマネージドAPIにまとめ、自前パイプラインの運用を不要にする。

## 使いどころ

- 住宅ローンや保険請求など、種類の混在する書類束を処理したいとき。
- 抽出値の監査可能性が求められる業務。
