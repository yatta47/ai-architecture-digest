---
type: case
title: DynamoDBのネイティブベクトル検索で運用データと埋め込みを1テーブルに統合したBedrockエージェント基盤
title_original: Build a unified AI agent architecture with DynamoDB and Bedrock
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- rag
- event-driven
components:
- Amazon DynamoDB
- Amazon Bedrock
- AWS Lambda
- Amazon DynamoDB Streams
- Amazon Titan Text Embeddings V2
outcome:
  type: cost
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/build-a-unified-ai-agent-architecture-with-dynamodb-and-bedrock/
published_at: '2026-08-21'
---

## 概要

運用データ用のDynamoDBとベクトル検索用の専用ストアを分離運用すると、二重管理によるコスト増や同期遅延で検索結果が古くなるという課題があった。2026年8月にGAしたDynamoDBのネイティブベクトル検索を使い、Bedrockエージェントが単一テーブルに対してCRUDと意味検索（SearchVectors）の両方を行うアーキテクチャに統合した。DynamoDB Streamsをトリガーに、コンテンツ更新時はTitan Text Embeddings V2で自動的に埋め込みを再生成し、ベクトルインデックスを常に最新に保つ。

## 設計のポイント

- ベクトルインデックスのパーティションキーには中程度のカーディナリティを持つ属性（例: category, tenant_id）を選び、極端に低い/高いカーディナリティを避ける
- DynamoDB Streamsで新規・更新イベントを捕捉し、埋め込み生成Lambdaを非同期でトリガーすることで、手動同期なしにベクトルインデックスを最新化する
- ベクトルインデックスの有効化にはオンデマンドキャパシティモードが必須で、1テーブルあたり最大5インデックス・次元数は最大4096という制約を設計時に織り込む
- インデックスがACTIVEになった直後の検索はValidationExceptionを返しうるためリトライ可能なエラーとして扱う

## 使いどころ

- 社内ナレッジ管理（ランブック・ADR・トラブルシューティングガイド）で自然言語質問への回答とドキュメントCRUDを同一エージェントに任せたい場合
- 運用データとセマンティック検索用データを別ストアで二重管理しており、インフラコストと同期の複雑さを削減したいチーム
- 会話型エージェントに構造化ルックアップと類似検索の両方のツール呼び出しをさせたいBedrockベースの開発者
