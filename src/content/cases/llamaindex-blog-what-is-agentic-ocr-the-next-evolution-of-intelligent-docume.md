---
type: guidance
title: エージェント型OCRが実現する自己修正型のドキュメント処理
title_original: What is Agentic OCR? The Next Evolution of Intelligent Document Processing
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
components: []
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/agentic-ocr
published_at: '2026-07-18'
---

## 概要

従来のOCRやIDP（Intelligent Document Processing）はレイアウトが変わると精度が劣化し、ドキュメントの意味を理解できない。エージェント型OCRはマルチモーダルLLMを推論層に据え、レイアウト理解・モデル選択・自己検証のループを回すことでテンプレート不要かつ数字の不整合を自動検出できる仕組みを実現する。

## 設計のポイント

- 複数の専門エージェント（レイアウト検出・表抽出・数値検証）を並列協調させ、統括するLLMがタスクを振り分ける
- 抽出したすべての値に元ページのバウンディングボックスを紐づけ、監査可能なトレーサビリティを確保する
- 内部整合性チェック（合計と明細の一致など）に失敗した場合、エージェントループ内で自己修正してから出力する

## 使いどころ

- レイアウトが頻繁に変わる請求書・契約書・医療フォームなど多様な書式を扱う自動化基盤
- 抽出結果の出典を数値単位で説明する必要があるコンプライアンス業務
