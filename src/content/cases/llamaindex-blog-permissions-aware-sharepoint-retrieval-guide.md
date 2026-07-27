---
type: guidance
title: SharePointの権限を引き継ぐパーミッション対応RAG検索
title_original: Permissions-aware content retrieval with SharePoint and LlamaCloud
company: LlamaIndex
industry: cross-industry
cloud:
- azure
patterns:
- multi-tenant-rag
- rag
- guardrails
components:
- LlamaParse
- LlamaCloud
- SharePoint
- OpenAI
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/permissions-aware-content-retrieval-with-sharepoint-and-llamacloud
published_at: '2026-07-20'
---

## 概要

LlamaParseのSharePoint連携が、SharePointの粒度の細かいアクセス制御をそのままRAGアプリの文書アクセス制御に使えるパーミッション対応機能を備えたことを示す手順解説。インデックス作成からSharePoint側の権限変更同期までの流れをステップバイステップで示す。

## 設計のポイント

- SharePointのアクセス制御情報をチャンク単位のメタデータ（allowed_siteUser_ids等）としてインデックスに同期し、RAGの検索結果に反映する
- 同期操作でSharePoint側の権限変更をインデックスに追従させ、常に最新の権限状態を保つ

## 使いどころ

- 組織内の機密文書を扱う社内向けRAGアプリで、ユーザーごとに閲覧可能な文書だけを検索結果に出したい場合
- SharePointを情報源とする既存の権限体系をそのままAI検索基盤に持ち込みたい企業
