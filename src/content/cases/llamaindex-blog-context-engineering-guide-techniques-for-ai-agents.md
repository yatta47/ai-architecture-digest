---
type: guidance
title: 「コンテキストエンジニアリング」で考えるAIエージェント設計の技法
title_original: What is Context Engineering and Techniques to Consider
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
- memory-consolidation
- rag
components:
- LlamaIndex
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider
published_at: '2026-07-19'
---

## 概要

プロンプトエンジニアリングより広い『コンテキストエンジニアリング』という概念を整理し、システムプロンプト・チャット履歴・長期記憶・知識ベース検索・ツール定義・構造化出力・ワークフロー状態など、エージェントのコンテキストウィンドウを構成する要素と、それを取捨選択・圧縮・並び替えする設計技法を解説する。

## 設計のポイント

- コンテキストウィンドウの制約を前提に、要約による圧縮や日付順の並び替えでLLMに渡す情報の優先順位を設計する
- ツール・知識ベースの選択自体もコンテキストの一部と捉え、エージェントがどのリソースを使うべきか判断できる情報を与える
- LlamaIndexのWorkflow Context（グローバルスクラッチパッド）でエージェントの複数ステップ間の状態を管理する

## 使いどころ

- 複数の知識ベースやツールを横断する複雑なエージェントを設計するAIエンジニア
- RAGだけでは説明できない、長期記憶や構造化出力を含む本格的なエージェント基盤を構築したい場合
