---
type: case
title: ベクトルDBなしでSEC提出書類を引用付き回答するデューデリジェンスエージェント
title_original: Building a Financial Due Diligence Agent with LiteParse
company: LlamaIndex
industry: financial-services
cloud: []
patterns:
- rag
- ai-agent
- document-processing
components:
- LiteParse
- Next.js
- Vercel AI SDK
- Claude
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-a-financial-due-diligence-agent-with-liteparse
published_at: '2026-07-18'
---

## 概要

アナリストが業務時間の最大70%を手作業のデータ転記に費やすSEC提出書類の分析業務に対し、約600行のNext.jsコードでベクトルDBや埋め込みパイプラインを使わずにLiteParseのバウンディングボックス情報だけで正確な引用ハイライトができるデモエージェントを構築した。回答は元PDFページ上の該当箇所をハイライト表示することで信頼性を担保する。

## 設計のポイント

- 文書集合が小規模（数十〜百件のフィリング）ならベクトル検索を使わずキーワードスコアリングと正規表現検索で十分とする
- LLMに引用箇所を<cite>タグで一字一句そのまま出力させ、逐語一致を前提にページ上の位置を逆算してハイライトする
- 厳密一致が失敗する場合に備えて空白許容マッチングなど複数の照合戦略を段階的に試すレイヤードマッチングを実装する

## 使いどころ

- SEC提出書類など大量ページの財務文書を根拠付きで検索・要約したいアナリスト業務
- 軽量なインフラで引用の信頼性を担保したいRAGアプリケーション
