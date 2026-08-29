---
type: announcement
title: SageMaker Feature Storeのバッチ書き込み・レコード探索API
title_original: Batch write and discover records in Amazon SageMaker Feature Store
industry: cross-industry
cloud:
- aws
patterns:
- feature-store-batch-ingestion
components:
- Amazon SageMaker Feature Store
- BatchWriteRecord
- ListRecords
- Amazon DynamoDB
- Redis
- Amazon Athena
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/batch-write-and-discover-records-in-amazon-sagemaker-feature-store/
published_at: '2026-08-28'
---

## 概要

Amazon SageMaker Feature Storeに、複数フィーチャーグループへ最大25件のレコードをまとめて書き込めるBatchWriteRecordと、オンラインストア内のレコード識別子を列挙できるListRecordsの2つのAPIが追加された。従来は1レコード1呼び出しのPutRecordループが高スループットなパイプラインでAPI呼び出し数のボトルネックとなり、In-Memoryストアではレコード識別子を失うと復旧不能という問題もあった。バッチAPIは部分成功セマンティクスとEventTimeベースの順序保証を維持したまま、これらの運用ギャップを埋める。

## 設計のポイント

- PutRecordのN×M呼び出しパターンをBatchWriteRecordで解消し、最大25件・複数フィーチャーグループを1コールにまとめてAPI呼び出しオーバーヘッドを削減する
- 個々のレコードが独立して成功/失敗するpartial-success設計とし、失敗分だけをErrors/UnprocessedEntriesとして返しリトライを容易にする
- EventTimeが既存レコードより新しい場合のみ最新版としてオンラインストアを更新し、そうでない場合はオフラインストアへ履歴として書くという既存の順序保証をバッチAPIでも継続する
- ListRecordsによりStandard(DynamoDB)/In-Memory(Redis)いずれの階層でもレコード識別子をページングで列挙できるようにし、In-Memory階層での識別子ロスによる永久喪失リスクに備える

## 使いどころ

- 秒間数万件規模でフィーチャーを更新する高スループットなリアルタイムMLパイプライン(不正検知など)でAPI呼び出し数を削減したい場合
- In-Memory(Redis)ストアを使っていてオフラインストアやAthenaのような代替手段がなく、レコードの棚卸し・監査・復旧手段を用意したい場合
