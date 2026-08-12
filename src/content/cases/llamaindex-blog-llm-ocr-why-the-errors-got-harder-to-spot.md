---
type: opinion
title: 流暢だが誤り:LLM OCRが起こす『見抜けない』誤読とその対策
title_original: 'LLM OCR: Why the Errors Got Harder to Spot'
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
components:
- olmOCR-Bench
- OmniDocBench
- GLM-OCR
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llm-ocr
published_at: '2026-08-12'
---

## 概要

LlamaIndexは『LLM OCR』が指すOCR事後補正・VLMネイティブ転記・エージェント的オーケストレーションという壊れ方の異なる3アーキテクチャを整理する。デコーダはピクセル証拠が弱いと言語の事前分布で埋めてしまうため、口座番号や合計金額のような高エントロピーな値ほど流暢だが誤った置換や、表の行が黙って欠落する現象が起き、従来の文字/単語誤り率では検出できないと指摘する。

## 設計のポイント

- 『LLM OCR』という言葉が指すOCR事後補正・VLMネイティブ転記・エージェント的オーケストレーションという3つの異なるアーキテクチャを区別し、それぞれ壊れ方が違うと整理した。
- デコーダはピクセル証拠が弱いとき言語の事前分布で埋めてしまうため、口座番号や合計金額のような高エントロピーな値ほど『流暢だが誤った』置換が起きやすいと指摘した。
- 文字/単語誤り率のような平均化指標ではなく、抽出値ごとにページ上の該当領域へのポインタを持たせるフィールド単位の証拠照合を評価指標にすべきだと提案した。

## 使いどころ

- LLM/VLMベースのOCRを導入する前に、ベンダーがどのアーキテクチャを採用しているか見極めたい調達担当者。
- 財務諸表や請求書など、桁や口座番号のような高エントロピーな値の誤りが致命的な業務でLLM OCRを使うチーム。
- 従来のCER/WERベンチマークがLLM OCRの実際の失敗モードを捉えられていないことに気づいた評価担当エンジニア。
