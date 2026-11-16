---
type: announcement
title: Bedrock Managed Knowledge Baseの表計算データ向けエージェント型検索(tabular search)
title_original: Get answers from tables with tabular search in Amazon Bedrock Managed Knowledge Base
industry: cross-industry
cloud:
- aws
patterns:
- rag
- ai-agent
- text-to-sql
components:
- Amazon Bedrock Managed Knowledge Base
- AgenticRetrieveStream
- Amazon S3
- Microsoft SharePoint
- Atlassian Confluence
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/get-answers-from-tables-with-tabular-search-in-amazon-bedrock-managed-knowledge-base/
published_at: '2026-11-16'
---

## 概要

Bedrock Managed Knowledge Baseがtabular searchに対応し、CSV/Excelの全行をネットワーク遮断のサンドボックスでモデル生成コードにより計算できるようになった。文書の根拠と表の計算結果を組み合わせて回答し、引用とトレースを返す。

## 設計のポイント

- 検索は表ファイルの特定に限り、全行の集計はコード実行に任せて分割テキストの欠落を避ける
- 元ファイルをネットワーク無しの隔離サンドボックスに置いて実行する
- 文書とデータを同じナレッジベースに置き、同一APIで文書事実と計算を組み合わせる
- ガバナンス対象の指標や大規模結合はBIツールに残す、と適用範囲を線引きする

## 使いどころ

- ポリシーと予算表を併用する財務の確認業務
- 文書と表が同居する社内ナレッジへの分析質問
