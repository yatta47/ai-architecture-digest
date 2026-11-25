---
type: announcement
title: 埋め込み・検索・生成をPostgres内で完結させRAG構成を単純化するPostgresML統合
title_original: Simplify your RAG application architecture with LlamaIndex + PostgresML
company: PostgresML
industry: cross-industry
cloud: []
patterns:
- rag
- unified-runtime
- inference-optimization
components:
- LlamaIndex
- PostgresML
- PostgreSQL
- PostgresML Managed Index
- Meta-Llama-3-8B-Instruct
- intfloat/e5-small-v2
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/simplify-your-rag-application-architecture-with-llamaindex-postgresml
published_at: '2024-05-28'
---

## 概要

LlamaIndexとPostgresMLの統合により、文書の保存・分割・埋め込み・検索・生成を単一システムで扱えるようになった。複数サービスへのネットワーク呼び出しを1回にまとめ、遅延と運用の複雑さを減らすことを狙う。

## 設計のポイント

- データをモデルへ運ぶのではなく、モデルをデータベース側に置いてネットワーク往復を減らす。
- 分割と埋め込みはDB側のパイプラインに任せ、アプリ側の前処理をなくす。
- オープンソースモデルをDB内で動かし、機密データを外部LLM事業者へ送らない構成にする。

## 使いどころ

- RAGの遅延や複数ベンダーの運用負荷を減らしたいチーム。
- 既にPostgreSQLを使っていて、AI機能を追加したい開発者。
