---
type: guidance
title: RAGでクエリ時にACLを検証して権限を守るアクセス制御
title_original: Rethinking access control for RAG with Amazon Quick and Amazon Bedrock
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- rag
- multi-tenant-rag
- defense-in-depth
components:
- Amazon Quick
- Amazon Bedrock Knowledge Bases
- Microsoft SharePoint
- Google Drive
- Confluence
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/rethinking-access-control-for-rag-with-amazon-quick-and-amazon-bedrock/
published_at: '2026-10-07'
---

## 概要

従来の同期してフィルタする方式の代わりに、クエリ時に元のデータソースへ権限を直接確認するリアルタイムACL検証を採る方式を解説する。権限のない文書が回答に混ざるリスクを抑える。

## 設計のポイント

- 定期同期のACLに頼らず、クエリ時に権威あるソースで権限を確認する。
- 権限変更が即時に回答へ反映される。

## 使いどころ

- SharePointやConfluenceなど権限の複雑な社内知識をRAG化する場面に効く。
