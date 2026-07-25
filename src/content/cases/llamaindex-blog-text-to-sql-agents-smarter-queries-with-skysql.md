---
type: case
title: SkySQLがLlamaIndexで実現するAgentic RAG方式のtext-to-SQLエージェント
title_original: How SkySQL Enables Smarter Text-to-SQL Agents with LlamaIndex
company: SkySQL
industry: cross-industry
cloud: []
patterns:
- text-to-sql
- rag
- human-in-the-loop
- ai-agent
components:
- LlamaIndex
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/how-skysql-enables-smarter-text-to-sql-agents-with-llamaindex
published_at: '2026-07-19'
---

## 概要

サーバーレスDBaaSのSkySQLは、テーブル数が多く曖昧なスキーマを持つ運用データベースに対する自然言語問い合わせで精度・セキュリティ・コストのトレードオフに課題を抱えていた。LlamaIndexをオーケストレーションエンジンに据えたAgentic RAGパイプラインと、開発者・DBAがエージェントの理解を修正できるExpert-in-the-Loopの仕組みを組み合わせ、高精度なtext-to-SQLエージェントを実現している。

## 設計のポイント

- テーブルスキーマ・サンプル行・プロンプト指示を含むリッチなコンテキストウィンドウをAgentic RAGパイプラインで自動構築し、LlamaIndexが検索と統合を担う
- 開発者・DBAがエージェントのコンテキスト（曖昧な関係やカラム名）を直接確認・修正できるExpert-in-the-Loopの仕組みを設け、修正内容を永続化して再利用する
- LLMに渡すメタデータ・サンプルデータの範囲をセキュリティ・ガバナンスの観点から厳密に制御する

## 使いどころ

- テーブル数が多く曖昧なスキーマを持つ運用データベースに自然言語で問い合わせたい場合
- SQL生成の精度・レイテンシ・コストのトレードオフを調整しながら本番運用したいDBaaS・データ基盤チーム
