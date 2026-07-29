---
type: case
title: コードリポジトリRAGの精度を高めるContext Refinement Agent
title_original: RAG Context Refinement
industry: manufacturing
cloud: []
patterns:
- rag
- ai-agent
- context-engineering
components:
- LlamaIndex
- Pinecone
- ChatGPT
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/rag-context-refinement-agent
published_at: '2026-07-25'
---

## 概要

コードリポジトリを対象としたRAGでは検索チャンクが文脈を欠きやすいという課題に対し、LLMエージェントが回答生成前にスクラッチパッド上のコンテキストを反復的に評価・修正するContext Refinement Agentを提案・試作した。半導体メーカーInfineonの公開リポジトリを題材にPoCを実施している。

## 設計のポイント

- 検索結果をそのままLLMに渡さず、Evaluatorステップがスクラッチパッドの十分性をスコアリングしてから最終回答を生成する
- 要約・チャンク除外・ファイル全体の取り込み・関連ドキュメントへのリンク追跡など複数のツールをTool Selectorが選択して適用する
- 制御フローを事前に固定せず、データに応じてどのツールを適用するか動的に決定する古典的Production Systemの構成を踏襲する

## 使いどころ

- コードやAPI・ファームウェアなど構造化されにくいドキュメントに対するサポート業務でのRAG精度向上
- 単純なtop-K検索では文脈が不足する技術サポート・カスタマーサポートのAI回答生成
