---
type: announcement
title: Lakeflow ConnectでSaaSの業務知識をUnity Catalogに取り込む
title_original: Unify your productivity and AI data with Lakeflow Connect
company: Databricks
industry: cross-industry
cloud: []
patterns:
- rag
- data-federation
- ai-agent
components:
- Lakeflow Connect
- Unity Catalog
- Jira
- Confluence
- SharePoint
- Google Drive
- GitHub
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/unify-your-productivity-and-ai-data-lakeflow-connect
published_at: '2026-10-26'
---

## 概要

Lakeflow ConnectのマネージドコネクターでAtlassian、Microsoft、Google Workspace、GitHubなどのデータをUnity Catalogに取り込み、構造化・非構造化データをエンタープライズ知識ベースやAIエージェントに使えるようにする。

## 設計のポイント

- 個別API連携を作らず、マネージドコネクターで増分取り込みする。
- 取り込み先をUnity Catalogに統一して一元的にガバナンスする。

## 使いどころ

- 社内文書を使うRAGやエージェントを作るデータチーム。
- 散在する業務ツールのデータを分析したい場合。
