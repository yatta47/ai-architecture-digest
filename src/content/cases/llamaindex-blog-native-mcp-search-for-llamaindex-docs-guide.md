---
type: announcement
title: LlamaIndexドキュメント向けネイティブMCP検索機能
title_original: Adding Native MCP to LlamaIndex Docs
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- full-text-search
- ai-agent
- document-processing
components:
- Vercel
- Claude Code
- OpenAI GPT-4.1
- PageFind
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/adding-native-mcp-to-llamaindex-docs
published_at: '2026-07-19'
---

## 概要

LlamaIndexは自社ドキュメントサイトにネイティブのMCPサーバーを追加し、search_docs（BM25全文検索）、grep_docs（正規表現検索）、read_doc（ページ全文取得）の3ツールを公開した。Vercel上でのデプロイ制約からベクトル検索(PageFind)の利用を断念し、ビルド時に静的なBM25転置インデックスを構築する軽量な方式を採用した。

## 設計のポイント

- コーディングエージェントが使い慣れたsearch/grep/readの3操作に合わせてツールを設計する
- 既存のドキュメント資産（Markdownページ）をそのまま再利用し、パス正規化ロジックだけを新規実装する
- 本番環境（Vercel）でロード可能かを検証したうえでベクトル検索ではなくBM25索引を選択する
- natural パッケージでトークナイズ/ステミングを行い、ビルド時に静的インデックスを生成してランタイムを軽量に保つ

## 使いどころ

- 自社ドキュメントをClaude CodeなどのコーディングエージェントからMCP経由で参照させたい開発者向けドキュメントサイト運営者
- LlamaIndexエージェントを構築する開発者が最新ドキュメントをエージェントのツールとして直接検索したい場面
