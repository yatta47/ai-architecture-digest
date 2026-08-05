---
type: announcement
title: Amazon Bedrockのサーバーサイド組み込みWeb検索によるモデルのグラウンディング
title_original: Introducing Web Search on Amazon Bedrock for foundation model grounding
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- rag
- context-engineering
components:
- Amazon Bedrock
- OpenAI Responses API
- Amazon Bedrock AgentCore
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-web-search-on-amazon-bedrock-for-foundation-model-grounding/
published_at: '2026-08-04'
---

## 概要

Amazon BedrockにサーバーサイドのWeb検索ツールが追加され、外部ベンダー統合なしにモデルの回答を最新のWeb知識で裏付けられるようになった。ナレッジグラフによる事実確認と意味的スニペット抽出でコンテキストを効率化し、既存のAWS認証情報のみで単一パラメータで有効化できる。

## 設計のポイント

- サーバーサイド組み込みツールとして提供し、クライアント側でのツール呼び出しループ実装や外部APIの管理を不要にする
- 事実確認的な質問にはナレッジグラフ、文脈が必要な質問にはWebページからの意味的スニペット抽出を使い分けて根拠を返す
- 既存のAWS IAM資格情報からSigV4経由で短命ベアラートークンを発行し、別途APIキー管理を不要にする
- デフォルトでゼロデータ流出とし、外部Webへのライブアクセスはオプトインのパラメータで切り替えられるようにする

## 使いどころ

- 最新情報が必要なチャットボットやコーディングアシスタントの回答をWeb知識で裏付けたい場合
- サードパーティ検索ベンダーの選定・統合・セキュリティレビュー工数を避けたいエンタープライズ
- 引用付きの根拠ある回答でハルシネーションを抑えたいエージェントアプリケーション
