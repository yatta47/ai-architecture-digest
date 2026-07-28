---
type: case
title: ハッカソン発のエージェント型RAGによる自動データクレンジングPoC「PureML」
title_original: 'PureML: Automated Data Clean-up and Refactoring'
company: PureML
industry: manufacturing
cloud: []
patterns:
- rag
- ai-agent
- event-driven
- document-processing
components:
- LlamaParse
- Pinecone
- OpenAI GPT-4
- LlamaIndex Workflow
- Reflex
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/pureml-automated-data-clean-up-and-refactoring
published_at: '2026-07-24'
---

## 概要

PureMLは、Agentic RAG-A-THONハッカソンで開発されたAIエージェントによるデータクレンジング自動化のPoC。自動車データセットを題材に、文脈を考慮した欠損値補完・新規特徴量の自動生成・表記ゆれのあるカテゴリの統合という3つのユースケースを、複数の専用エージェントとイベント駆動のワークフローで実現した。

## 設計のポイント

- LlamaParseで複雑なPDF資料をMarkdown化しPineconeへ格納することでRAGの検索精度を担保する
- 単発のRAG検索では不十分なため、複数ツールを備えたエージェント型RAGで文脈依存の判断を行う
- LlamaIndex Workflowのイベント駆動アーキテクチャで、用途ごとに異なる専用エージェントを疎結合に連携させる
- ユースケースごと（欠損値補完・特徴量生成・カテゴリ統合）に別々のエージェントを割り当てて複雑さを分離する

## 使いどころ

- モデル構築前の手作業によるデータクレンジングにコストと時間を取られているMLチーム
- 欠損値を単純平均で埋めるのではなく文脈を踏まえて補完したいデータセット
- 表記ゆれのあるカテゴリ（例: 『Chevy』と『Chevrolet』）を統合し一貫性を確保したい場合
- 既存データに存在しない特徴量を行レベルの文脈から新たに生成したいケース
