---
type: announcement
title: 動画・画像を自然言語で意味検索できるマルチモーダルナレッジベース
title_original: Video and image search in Amazon Bedrock Knowledge Base using Marengo 3.0
industry: cross-industry
cloud:
- aws
patterns:
- rag
- video-intelligence
components:
- Amazon Bedrock Knowledge Bases
- TwelveLabs Marengo Embed 3.0
- Amazon S3
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/video-and-image-search-in-amazon-bedrock-knowledge-base-using-marengo-3-0/
published_at: '2026-09-10'
---

## 概要

Amazon Bedrock Knowledge BasesにTwelveLabsのMarengo Embed 3.0が組み込まれ、動画・画像・音声を含むマルチモーダルコンテンツを自然言語で意味検索できるようになった。フレーム抽出や文字起こし、埋め込み生成、ベクトルインデックス化をフルマネージドで行い、S3にアップロードするだけでRAGパイプラインを構築できる。

## 設計のポイント

- 動画・音声・画像・テキストを512次元の単一ベクトル空間に統合するマルチモーダル埋め込みモデルを採用する
- フレーム抽出・文字起こし・セグメンテーションをマネージド化し、利用者側の前処理パイプライン構築を不要にする
- 既存のBedrock Retrieve APIやAgentCoreのGatewayターゲットとして接続し、下流アプリケーションに組み込みやすくする

## 使いどころ

- スポーツ映像から特定のプレーを自然言語で検索したい分析チーム
- 防犯カメラ映像から特定インシデントを検索したいセキュリティ担当
- 講義動画を概念単位で検索したい教育コンテンツ運営者
