---
type: announcement
title: Rayでの高速化・再帰検索・メタデータ抽出などの更新（2023-07-10）
title_original: LlamaIndex Update 07/10/2023
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- text-to-sql
- document-processing
components:
- LlamaIndex
- Ray
- Ray Serve
- DuckDB
- Chainlit
- DePlot
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-update-07-10-2023-4ceebdab96cb
published_at: '2023-07-10'
---

## 概要

Anyscale/Ray連携、メタデータ管理の刷新、再帰検索、text-to-SQL改善、自動メタデータ抽出などを紹介する更新情報。

## 設計のポイント

- 表などは要約ノードから専用クエリエンジンへ辿る再帰検索で扱う。
- 埋め込み用とLLM用で渡すメタデータを個別に制御する。
- テーブル数が多いDBはスキーマを索引化し、関連表だけを選んでSQLを生成する。

## 使いどころ

- 構造の複雑な文書や大規模スキーマを扱うRAG開発者向け。
- LlamaIndexの更新内容を把握したいチーム向け。
