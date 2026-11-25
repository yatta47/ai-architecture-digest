---
type: announcement
title: LlamaParseにチャットUI・組織機能・コネクタを追加
title_original: The Latest Updates to LlamaCloud
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- LlamaParse
- create-llama
- Notion
- Slack
- Jira
- SharePoint
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/the-latest-updates-to-llamacloud
published_at: '2024-07-19'
---

## 概要

データに対して数分でチャットできるLlamaParse Chat、組織単位でパイプラインを共有する機能、Notion・Slack・Jiraのコネクタを追加した。SharePointコネクタはユーザーIDで絞り込め、アクセス制御に使える。

## 設計のポイント

- 索引済みパイプラインを組織で共有し、各自の再索引を避ける。
- ユーザーIDのメタデータで検索を絞り、アクセス制御を実現する。

## 使いどころ

- 社内データのRAGを複数人で開発するチーム。
- 権限を考慮した社内検索を作りたい場合。
