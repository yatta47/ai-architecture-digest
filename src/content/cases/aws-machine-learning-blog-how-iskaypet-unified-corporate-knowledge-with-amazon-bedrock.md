---
type: case
title: IskayPetのBedrock Managed Knowledge Basesによる4言語の社内ナレッジアシスタント
title_original: How IskayPet unified corporate knowledge with Amazon Bedrock Managed Knowledge Bases
company: IskayPet
industry: retail
cloud:
- aws
patterns:
- rag
- multilingual-localization
- multi-tenant-rag
- spec-driven-development
components:
- Amazon Bedrock Managed Knowledge Bases
- Microsoft SharePoint
- Kiro
- Claude Haiku 4.5
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-iskaypet-unified-corporate-knowledge-with-amazon-bedrock-managed-knowledge-bases/
published_at: '2026-10-22'
---

## 概要

ペットケア大手IskayPetは、SharePointの文書を対象に、ベクトルDBや取り込みパイプラインを自前運用しない社内ナレッジアシスタントを構築した。4言語・3カ国で小売、獣医、人事、調達の質問に答える。フロントからデプロイまでKiroとClaude Haiku 4.5で開発した。

## 設計のポイント

- Managed Knowledge Basesを使い、RAG基盤の運用を持たない構成にしている。
- 領域・国ごとに知識を振り分け、相互汚染を避ける。
- SharePointを情報源として統合し、4言語を単一システムで扱う。
- 新しい領域や国を再設計なしで追加できる構成を要件とした。

## 使いどころ

- 多言語・多拠点の社内規程やマニュアルを検索可能にしたい企業。
- RAG基盤を運用せずに知識アシスタントを立ち上げたい小規模チーム。
