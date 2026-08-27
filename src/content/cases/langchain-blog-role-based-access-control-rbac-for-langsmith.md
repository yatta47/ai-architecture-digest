---
type: announcement
title: LLMOps基盤LangSmithへのロールベースアクセス制御とAPIキー分離
title_original: Access Control Updates for LangSmith
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- LangSmith
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/access-control-updates-for-langsmith
published_at: '2026-08-26'
---

## 概要

LangSmithにワークスペース単位のロールベースアクセス制御（RBAC）とカスタムロール機能が追加され、Admin/Viewer/Editorなどの権限を細かく設定できるようになった。あわせてユーザーに紐づく個人アクセストークンとサービスに紐づくサービスキーを分離し、組織変更や離脱の影響を受けにくいAPIキー運用を可能にした。

## 設計のポイント

- ワークスペース単位でAdmin/Viewer/Editorのビルトインロールに加えカスタムロールを定義できるようにし、最小権限の原則を運用しやすくした
- ユーザーに紐づく個人アクセストークンと、サービス自体に紐づくサービスキーを分離し、担当者の異動・離脱に強い認証設計にした

## 使いどころ

- 複数チームでLLMOps基盤を共有する際のアクセス権限設計
- 監査要件が厳しいエンタープライズ組織でのAPIキー運用
