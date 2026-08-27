---
type: case
title: PostgreSQL単体でRAG・時系列コンテキスト検索を高速化するTimescale Vector
title_original: 'Timescale Vector x LangChain: Making PostgreSQL A Better Vector Database for AI Applications'
company: Timescale
industry: cross-industry
cloud: []
patterns:
- rag
components:
- Timescale Vector
- PostgreSQL
- pgvector
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/timescale-vector-x-langchain-making-postgresql-a-better-vector-database-for-ai-applications
published_at: '2026-08-26'
---

## 概要

Timescale VectorはDiskANNに着想を得た独自索引でpgvectorより大幅に高速な類似検索を実現しつつ、ハイパーテーブルの時系列パーティショニングを活用した「時間で絞り込むベクトル検索」を提供するLangChain連携を発表した。ベクトル・リレーショナル・時系列データを単一のPostgreSQLに集約することで、複数のデータベース製品を組み合わせる運用の複雑さを解消している。

## 設計のポイント

- ベクトル・リレーショナル・時系列データを別々のデータベース製品に分散させず単一のPostgreSQLに統合し、AI基盤の運用を簡素化した
- DiskANNに着想を得た独自索引とプロダクト量子化により、pgvector比で大幅な索引省スペース化と検索高速化を実現した
- Timescaleのハイパーテーブルによる時間ベースの自動パーティショニングを生かし、直近のデータや期間指定でベクトル検索を絞り込めるようにした

## 使いどころ

- 既にPostgreSQLを使っておりベクトルDBを別途増やさずRAGを実現したいチーム
- チャット履歴や時系列データとベクトル検索を組み合わせた時間軸付きRAGを構築したい開発者
