---
type: guidance
title: OCR精度の測り方と改善方法:CER・WER・フィールド精度の実務ガイド
title_original: 'OCR Accuracy Explained: How to Improve It'
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
components: []
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/ocr-accuracy
published_at: '2026-07-18'
---

## 概要

OCR精度をCharacter Error Rate・Word Error Rate・フィールドレベル精度という3層の指標で計測する方法と、解像度・レイアウト複雑性・手書き・ハードウェア制約・文書の劣化状態が精度に与える影響を整理。金融フィールドでは99.9%のフィールド精度がストレートスルー処理を実現する閾値になると解説する。

## 設計のポイント

- 用途に応じてCER/WER/フィールド精度のどれを最適化指標にするか使い分ける
- スキャン解像度など安価に改善できる前処理要因を優先的に是正する
- レイアウト理解型のパーサーで多列・表・透かしなど複雑な構造に対応する

## 使いどころ

- 請求書処理やKYCなどストレートスルー処理を目指す高精度要求のワークフロー
- OCRベンダーやパイプラインを比較評価したいドキュメントAI担当者
