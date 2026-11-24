---
type: announcement
title: 'LlamaIndex: AutoRAGと知識グラフのエージェント戦略'
title_original: LlamaIndex Newsletter 2025-01-21
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- eval
- text-to-sql
- ai-agent
components:
- AutoRAG
- LlamaParse
- AWS Bedrock
- Memgraph
- Hugging Face
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-01-21
published_at: '2025-01-21'
---

## 概要

RAGパイプライン最適化のAutoRAG（ハイブリッド検索の優位性など）、text2cypherのエージェント戦略、多言語ビジュアル埋め込みモデル公開を扱うニュースレター。

## 設計のポイント

- 構成を比較評価し、ハイブリッド検索や再ランカの効果を検証してから採用する
- text2cypherで再試行と自己修正を行う
- 多言語ビジュアル埋め込みでトークン数を減らし推論を高速化する

## 使いどころ

- RAG構成の最適なパラメータを選びたい場面
- グラフDBへの自然言語クエリ精度を上げたい場面
