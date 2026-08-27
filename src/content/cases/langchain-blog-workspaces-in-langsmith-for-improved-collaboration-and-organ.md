---
type: announcement
title: LangSmithにワークスペース機能を追加、組織内のLLM開発リソースをチーム単位で分離
title_original: Workspaces in LangSmith for improved collaboration and organization
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- policy-as-code
components:
- LangSmith
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/workspaces-in-langsmith
published_at: '2026-08-25'
---

## 概要

LangChainのLLMオブザーバビリティ/評価プラットフォームLangSmithに、組織内のユーザーとリソースを論理的にグルーピングする「ワークスペース」機能が追加された。トレースプロジェクトやデータセット、プロンプトなどは単一ワークスペースに紐づくようになり、組織単位のロール管理とRBACによるワークスペース単位の権限付与を組み合わせて、チームや事業部、デプロイ環境ごとにLLM開発リソースを分離できる。

## 設計のポイント

- トレース・データセット・プロンプトなどのリソースを組織全体で共有せず、単一ワークスペースに紐づけることでチーム/環境間のアクセスを分離する
- 組織管理者（全ワークスペースにAdmin権限）と組織ユーザー（ワークスペース単位でRBACロールを付与）という2層のロールモデルで、統制と柔軟性を両立する
- APIキーをワークスペース単位でスコープすることで、認証情報の影響範囲をそのチーム・環境内に閉じ込める

## 使いどころ

- 複数チーム・事業部が同時にLLM/エージェントプロジェクトを走らせ、データセットやトレースを分離したいエンタープライズ
- 本番・検証など複数のデプロイ環境ごとにLLM関連リソースへのアクセスを切り分けたいプラットフォームチーム
