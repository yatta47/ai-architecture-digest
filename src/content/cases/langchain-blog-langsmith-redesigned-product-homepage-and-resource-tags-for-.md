---
type: announcement
title: 観測性・評価・プロンプトエンジニアリングで再構成したLangSmithホームページとリソースタグ
title_original: 'LangSmith: Redesigned product homepage and Resource Tags for better organization'
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- LangSmith
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-homepage-redesign-and-resource-tags
published_at: '2026-06-16'
---

## 概要

LangSmithのプロダクトホームページを観測性・評価・プロンプトエンジニアリングの3領域に再構成し、リソースタグによってトレーシングプロジェクト・データセット・プロンプトをアプリや環境単位で横断的に整理できるようにした。

## 設計のポイント

- 観測性・評価・プロンプトエンジニアリングという開発ワークフローの3領域でプロダクト構成を明確に分離する
- リソースタグによって環境(dev/staging/prod)やアプリ単位でトレーシングプロジェクト・データセット・プロンプトを横断的にグルーピングする

## 使いどころ

- 複数のLLMアプリや環境をまたいでリソースを整理したいチーム
- 観測性・評価・プロンプト管理を一つのワークフローとして統一したい場合
