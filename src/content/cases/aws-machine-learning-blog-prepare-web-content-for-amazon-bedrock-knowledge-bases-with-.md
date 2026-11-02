---
type: guidance
title: Bedrock Knowledge BasesへのWebコンテンツ取り込みをCrawl4AIで前処理する構成
title_original: Prepare web content for Amazon Bedrock Knowledge Bases with Crawl4AI
industry: cross-industry
cloud:
- aws
patterns:
- rag
- document-processing
components:
- Amazon Bedrock Knowledge Bases
- Crawl4AI
- AWS Fargate
- Amazon S3
- Amazon EventBridge
- AWS Systems Manager Parameter Store
- AWS CDK
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/prepare-web-content-for-amazon-bedrock-knowledge-bases-with-crawl4ai/
published_at: '2026-11-02'
---

## 概要

標準のBedrock Web Crawlerで足りない場合に、Crawl4AIで本文抽出・ボイラープレート除去・独自メタデータ付与を行ってからS3経由でナレッジベースに取り込む構成を解説する。EventBridge起動のFargateタスクがクロール、S3アップロード、取り込みジョブ開始までを順に実行する。

## 設計のポイント

- まずは標準のWeb Crawlerを使い、本文領域の限定や独自メタデータが必要なソースだけ前処理パスに振り分ける。
- Markdown本文とメタデータのサイドカーをページ単位でS3に置き、チャンク化以降はマネージドなナレッジベースに任せて責務を分離する。
- クロールは深さ・ページ数・URLパターン・スコープで上限を設け、robots.txtを尊重して意図しない拡散を防ぐ。

## 使いどころ

- サイト由来のナビゲーションなどのノイズを除いてRAGの検索品質を上げたい場合。
- 取り込み文書に独自属性を付け、検索結果をメタデータで絞り込みたい場合。
- 公開Webサイトを定期バッチでナレッジベースに同期したいチーム。
