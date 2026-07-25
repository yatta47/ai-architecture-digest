---
type: guidance
title: 文書分類が当たらないのはモデルではなく抽出層(OCR)が原因という設計論
title_original: 'OCR Document Classification: A Developer''s Guide'
company: LlamaIndex
industry: cross-industry
cloud:
- aws
patterns:
- document-processing
components:
- LlamaParse
- Tesseract
- AWS Textract
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/ocr-document-classification
published_at: '2026-07-19'
---

## 概要

文書分類の失敗はモデルのチューニング不足として扱われがちだが、実際にはOCRが返す崩れたテキストや失われたレイアウト構造が原因であることが多いと指摘する。LlamaParseは要素ごとに文字認識・表用のビジョンモデル・レイアウト保持を使い分けるエージェント型オーケストレーションで抽出層を強化し、信頼度スコアと引用付きの検証可能な出力を分類層に渡す設計を紹介する。

## 設計のポイント

- 分類精度が低いときはまず抽出層(OCR)の出力品質を疑い、分類モデル側のチューニングから始めない
- 文書要素ごとに最適な処理(テキストはOCR、表や画像はビジョンモデル)を振り分けるエージェント型オーケストレーションを採用する
- 抽出結果に信頼度スコア・ページ領域への引用・バウンディングボックスを付与し、人間によるレビューをボトルネックにせず要所だけ回せるようにする
- テンプレート変更やスキャン品質のばらつきで抽出精度が無音劣化する『メンテナンスの踏み車』を、モニタリングなしの初期設定放置で招かないようにする

## 使いどころ

- 受信文書を自動でキューに振り分けるバックオフィスの文書分類パイプライン
- 分類モデルのエラーを追っても改善しない状況で、上流の抽出品質を疑いたいエンジニア
