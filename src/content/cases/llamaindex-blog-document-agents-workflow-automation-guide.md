---
type: guidance
title: LlamaParseとLlamaIndexで銀行文書に答えるツール統合エージェントを構築するチュートリアル
title_original: 'Automate Workflows with Document Agents: A Complete Tutorial to Building Context-Aware AI'
industry: financial-services
cloud: []
patterns:
- rag
- ai-agent
- document-processing
- context-engineering
components:
- LlamaParse
- LlamaIndex
- LlamaParseIndex
- FunctionAgent
- QueryEngineTool
- Claude Sonnet 4
- LlamaCloud
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/automate-workflows-with-document-agents-a-complete-tutorial-to-building-context-aware-AI
published_at: '2025-08-24'
---

## 概要

JPMorgan Chaseの預金口座開示・料金規約文書を題材に、LlamaParse Indexで文書を解析・インデックス化し、Claude Sonnet 4を用いたクエリエンジンで基本的なRAG応答を実現する手順を示す。さらにLlamaIndexのFunctionAgent（Workflows）で計算ツールと文書検索ツールを組み合わせ、複数の手数料条件が絡む複合的な銀行実務質問に多段階で回答するエージェントを構築している。

## 設計のポイント

- まず単純な検索・基本RAGで動作確認してから、ツール統合エージェントへ段階的に拡張する
- 文書検索をQueryEngineToolとして独立化し、計算ツールなど他のツールと疎結合に組み合わせる
- FunctionAgentのstream_eventsでツール呼び出しと推論過程をリアルタイムに可視化してデバッグしやすくする
- system_promptでエージェントの専門領域（銀行手数料・手続き）を明示し、ツール選択の精度を高める

## 使いどころ

- 銀行の規約集や開示文書など、複数箇所の参照と計算を要する複合質問に答えるカスタマーサポートエージェント
- 単純な文書検索だけでは対応できない、条件分岐や日付・手数料計算を伴うエンタープライズ文書QA
- PDFなど非構造化文書を実務で使えるインテリジェントエージェントに変換したい開発者向けの実装手順
