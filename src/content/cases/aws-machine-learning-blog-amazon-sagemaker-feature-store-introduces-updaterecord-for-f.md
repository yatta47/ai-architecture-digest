---
type: announcement
title: SageMaker Feature StoreのUpdateRecordでML特徴量を部分更新
title_original: Amazon SageMaker Feature Store introduces UpdateRecord for feature-level writes
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
components:
- Amazon SageMaker Feature Store
- Amazon DynamoDB
- Amazon ElastiCache
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-feature-store-introduces-updaterecord-for-feature-level-writes/
published_at: '2026-09-08'
---

## 概要

Amazon SageMaker Feature StoreにUpdateRecord APIが追加され、特徴量グループの一部の値だけを読み取りなしでアトミックに更新できるようになった。従来のGetRecord→マージ→PutRecordという読み取り・変更・書き込みサイクルを排除し、レイテンシとRCUコストを削減しつつ複数パイプラインの同時書き込みによる競合（lost update）も防ぐ。

## 設計のポイント

- 部分更新（変更フィールドのみ送信）でRead-Modify-Write型のロストアップデート問題を構造的に排除する
- オンラインストア（低レイテンシ）とオフラインストア（学習用フルスナップショット）を非同期で同期させ両者の役割を分離する
- EventTimeの順序チェックで古い書き込みを409エラーとして拒否し整合性を保証する
- 新ストレージ形式への移行はバルク再取り込みとin-place切替の2戦略を用意しダウンタイム許容度に応じて選べるようにする

## 使いどころ

- 不正スコアリングなど複数パイプラインが同一レコードの異なる特徴量を並行更新するMLシステム
- 高頻度更新かつワイドな特徴量グループを持ちRCUコストが課題になっているチーム
- 低レイテンシなオンライン推論と学習用オフラインデータの両方を同じ特徴量ストアで賄いたい場合
