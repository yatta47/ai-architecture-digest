---
type: case
title: 自然言語の要件からクラウド構成図と料金見積りを生成するRAGformation
title_original: 'Automatically generating cloud configurations: introducing RAGformation'
industry: cross-industry
cloud:
- aws
patterns:
- rag
- ai-agent
- multi-agent-orchestration
components:
- LlamaIndex Workflows
- Pinecone
- Box
- LlamaParse
- Toolhouse
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/automatically-generating-cloud-configurations-introducing-ragformation
published_at: '2026-07-23'
---

## 概要

LlamaIndex RAG-a-thonで受賞したRAGformationは、ユーザーが自然言語で入力した要件をLlamaIndexのエージェントオーケストレーターが解釈し、Pineconeにベクトル化されたAWSアーキテクチャ知識ベースから最適なクラウドサービス構成とフロー図、料金見積りを自動生成するツール。要件変更に応じて構成を動的に再提案する。

## 設計のポイント

- 設計知識（ブログ記事・論文・クラウドドキュメント）をBoxに集約しLlamaParseで解析してPineconeベクトルストアに投入する
- LlamaIndexベースのオーケストレーターがユーザー対話・料金計算・図生成の各エージェントを制御するマルチエージェント構成にする
- AWSの料金APIをリアルタイムに呼び出してアーキテクチャ提案と同時にコスト見積りを提示する

## 使いどころ

- クラウドサービス選定や見積りに数日〜数週間かかっている企業の導入検討チーム
- 手書きのアーキ図スケッチから構成を素早く具体化したいエンジニア
