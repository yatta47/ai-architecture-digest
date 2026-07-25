---
type: announcement
title: ParseBenchベンチマークとセルフホスト型LiteParse-Serverの発表
title_original: LlamaIndex Newsletter 5-19
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
components:
- LiteParse
- LiteParse-Server
- ParseBench
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-5-19-26
published_at: '2026-07-18'
---

## 概要

LlamaIndexの週次ニュースレターで、AIエージェント向けに設計された初のドキュメントOCRベンチマーク「ParseBench」のウェビナー告知と、セキュアなサンドボックス環境でLiteParseを使えるRust製CLIエージェント「Sandboxed-Lit」、完全ローカルで動くセルフホスト型のLiteParse-Serverが紹介されている。

## 設計のポイント

- 既存のOCRベンチマークがAIエージェントの実際の要求（構造保持など）を反映していないという課題意識からParseBenchを設計する
- ドキュメント解析をサンドボックス内で実行し、ファイルシステムアクセスを保ちながらセキュリティを担保する

## 使いどころ

- ドキュメント取り込みパイプラインの精度を定量的に評価したいチーム
- プライベート環境で完結する自己ホスト型のドキュメント解析基盤を求める企業
