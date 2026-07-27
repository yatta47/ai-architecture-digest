---
type: guidance
title: Text2CypherをWorkflowで反復改善するナレッジグラフRAGエージェント
title_original: Building Knowledge Graph Agents with LlamaIndex Workflows
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
- eval
components:
- LlamaIndex Workflows
- Neo4j
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-knowledge-graph-agents-with-llamaindex-workflows
published_at: '2026-07-19'
---

## 概要

Neo4jなどのグラフDBに対する自然言語クエリをCypherへ変換するtext2cypherの精度課題に対し、単純フローからリトライ付き・評価付き・反復プランナー付きフローへ段階的に強化する設計をLlamaIndex Workflowsで示す。ベンチマークで各手法の精度差を比較している。

## 設計のポイント

- 生成したCypherの実行結果を評価し失敗時にリトライするループを組み込む
- GoogleBLEUだけでなく実行結果が一致するExactMatchで正しさを検証する
- 反復プランナーで質問を段階的に分解し複雑なグラフクエリの精度を高める

## 使いどころ

- 構造化データ（グラフDB）をRAGに組み込みたいチームのtext2cypher設計
- 自然言語からのクエリ生成精度を本番投入前にベンチマークしたい場合
