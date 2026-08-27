---
type: announcement
title: 単一APIキーで複数LLM・AIサービスを切り替えるEden AIのLangChainゲートウェイ連携
title_original: 'Eden AI x LangChain: Harnessing LLMs, Embeddings, and AI'
company: Eden AI
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- llm-gateway
components:
- Eden AI
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/eden-ai-x-langchain
published_at: '2026-08-26'
---

## 概要

Eden AIは複数のLLM・埋め込み・OCR・画像解析などのAIサービスを単一のAPIキーで扱えるゲートウェイをLangChainに統合し、LangChainがネイティブに対応していないモデルプロバイダーへのアクセスやコスト・利用状況の一元的なダッシュボード管理を可能にした。LangChainのAgent Toolsとも統合されており、コンテンツ検知や帳票解析などの機能をエージェントのツールとしてそのまま組み込める。

## 設計のポイント

- 複数のLLM/埋め込みプロバイダーへのアクセスを単一のAPIキー・単一のインターフェースに集約するゲートウェイ層をLangChainの手前に置いた
- 利用状況とコストを横断的に可視化するダッシュボードとAPIキャッシュを提供し、重複課金や予算超過を防ぐ設計にした
- OCRや帳票解析、コンテンツ検知などの周辺AI機能をLangChain Agentのツールとして直接呼び出せるようにし、エージェントの機能を拡張した

## 使いどころ

- 複数のLLM/AIベンダーを使い分けたいがそれぞれの認証・課金管理を個別にしたくないチーム
- LangChain未対応のモデルプロバイダーやOCR等の周辺AI機能をエージェントのツールとして使いたい開発者
