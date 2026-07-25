---
type: announcement
title: LlamaIndex 2025年9月ニュースレターまとめ
title_original: LlamaIndex Newsletter 9-30-25
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- rag
components:
- Claude Code
- Qdrant
- OpenAI
- Next.js
- LlamaIndex Workflows
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-09-30
published_at: '2026-07-19'
---

## 概要

LlamaIndexの2025年9月版ニュースレターで、Claude Codeにドキュメント理解能力を追加する手法、LlamaIndex WorkflowsとNext.js・Qdrantを組み合わせたフルスタックエージェントのサンプル、ベルリンのVector Space Dayでのベクトル検索を用いたエージェントメモリに関する講演などが紹介された。

## 設計のポイント

- コーディングエージェントには標準機能では扱えないPDF/契約書向けに、MCPやCLI、エージェント生成ワークフローなど専用の文書理解ツールを組み込む
- LlamaIndex Workflows + Next.js + QdrantでフルスタックのRAGエージェント参照実装を構成する
- ベクトル検索を使ってエージェントワークフローにステートフルな記憶レイヤーを追加する

## 使いどころ

- Claude CodeでPDFや契約書を扱う社内ツールを構築するチーム
- ベクトルDBを使ったフルスタックRAGチャットアプリを試作したい開発者
