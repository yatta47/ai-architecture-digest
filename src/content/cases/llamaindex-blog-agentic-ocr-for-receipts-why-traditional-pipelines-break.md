---
type: guidance
title: レシートOCRが破綻する理由とエージェント型パースへの転換
title_original: 'Agentic OCR for Receipts: Why Traditional Pipelines Break'
industry: retail
cloud: []
patterns:
- document-processing
- ai-agent
components:
- LlamaCloud
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/ocr-for-receipts
published_at: '2026-07-18'
---

## 概要

レシートは店舗ごとにフォーマットが標準化されておらず、伝統的なOCR→正規表現→手直しのパイプラインはルールの増殖で破綻しやすい。LlamaCloudはVLMベースのエージェント型OCRとして、レイアウト理解・構造推論・検証を単一システムで行い、明細のグルーピングや小計/合計の意味的な区別を実現する。

## 設計のポイント

- レイアウト認識・視覚言語モデル・言語モデルによる構造推論・検証ループを1つの協調システムに統合する
- 小計と合計を数値の大小だけでなく意味的な役割で区別する
- 抽出結果に信頼度スコアとメタデータを付与し、必要な箇所だけ人間のレビューに回す

## 使いどころ

- 店舗ごとにフォーマットが異なる大量のレシートを継続的に処理する経費精算・小売分析
- テンプレートメンテナンスのコストを増やさずに新しい店舗フォーマットへ対応したい場合
