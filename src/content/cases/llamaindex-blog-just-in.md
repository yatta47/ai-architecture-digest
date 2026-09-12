---
type: guidance
title: 検索してからVLMで必要なページだけ読む二段階OCRパターン
title_original: Just-in-Time Agentic OCR
industry: financial-services
cloud: []
patterns:
- document-processing
- rag
- context-engineering
components:
- LlamaParse
- LiteParse
- Claude Cowork
- Opus 5
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/just-in-time-agentic-ocr
published_at: '2026-09-12'
---

## 概要

LlamaIndexは、データルーム型のドキュメントAIエージェントで広がりつつある『二段階OCR』パターンを解説する。まず全ファイルを無料/OSSツールで軽量にパースして検索対象を作り、検索でヒットしたページだけをVLMで高精度に読み直すことで、精度を保ちながらコストと速度を両立する。FinanceBenchの84件のSEC提出書類・12,013ページに適用した例では、全体スキャンが32秒、VLM再パースは該当2ページのみで完了した。

## 設計のポイント

- 全文書に高コストなVLM-OCRをかけるのではなく、まず軽量パースで検索可能なインデックスを作り、必要なページだけ後からVLMで『ズームイン』する
- 10〜100文書程度のアドホックなデータルームでは二段階OCRが有効だが、1,000〜100万文書規模のオフラインパイプラインでは検索精度がテキスト表現の質に依存するため事前に全ページVLM-OCRをかけるべき
- ページ単位で複雑度（needs_ocr等）を判定するツールを使い、VLM処理が必要なページを事前に絞り込む

## 使いどころ

- 少数〜中規模のアップロード文書に対してアドホックな質問応答を行うドキュメントエージェントを構築する場合
- 財務諸表など複雑な表を含むページのみ高精度な解析が必要なデューデリジェンス業務
