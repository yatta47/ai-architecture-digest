---
type: case
title: PostgreSQLベースの単一サービスでベクトル検索と会話メモリを両立するXata連携
title_original: 'Xata x LangChain: new vector store and memory store integrations'
company: Xata
industry: cross-industry
cloud: []
patterns:
- rag
components:
- Xata
- PostgreSQL
- Elasticsearch
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/xata-x-langchain-new-vector-store-and-memory-store-integrations
published_at: '2026-08-26'
---

## 概要

PostgreSQLを正とし裏でElasticsearchに複製するデータベース基盤Xataが、LangChainのベクトルストアおよびチャット履歴（メモリ）ストアとして統合された。1つのサーバーレスAPIの裏でPostgreSQLのACID特性とElasticsearchのベクトル/全文検索の両方を使えるため、社内データに基づく会話型Q&Aボットを1つのデータ基盤で完結して構築できる。

## 設計のポイント

- 正のデータをPostgreSQLに置きながら裏でElasticsearchへ自動複製する構成にし、1つのサーバーレスAPIでACIDトランザクションとベクトル/全文検索の両方を提供した
- 同じXata基盤をベクトルストアとチャット履歴（メモリ）ストアの両方として使い、会話型Q&Aアプリのデータ層を1サービスに集約した
- メタデータをXataのカラムとして表現しフィルタリングできるようにし、ベクトル検索とメタデータ絞り込みの性能を両立した

## 使いどころ

- 社内データに基づく会話型Q&A（chat with your data）をシンプルなデータ基盤で構築したいチーム
- ベクトルストアと会話履歴用ストレージを別々に運用する複雑さを避けたい開発者
