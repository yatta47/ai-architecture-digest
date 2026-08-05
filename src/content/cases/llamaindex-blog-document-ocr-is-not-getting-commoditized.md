---
type: case
title: 難易度ルーティングとRL特化学習でフロンティアVLMを上回るドキュメントOCRパイプライン
title_original: Document OCR is not getting commoditized
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- reinforcement-learning
- inference-optimization
- eval
components:
- LlamaParse
- ParseBench
- PDFium
- LiteParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/document-ocr-is-not-getting-commoditized
published_at: '2026-08-05'
---

## 概要

LlamaIndexは、フロンティアモデルが推論性能ばかり強化されドキュメント読解が相対的に弱いままである点を独自ベンチマークParseBenchで示し、専用OCRエンジンLlamaParseの方が精度・コストともに優れると主張する。ページ難易度に応じたモデル振り分け、検証可能な報酬によるRL特化学習、PDF内蔵テキストの直接活用を組み合わせて実現している。

## 設計のポイント

- ページごとの難易度を学習したルーティングモデルで判定し、フロンティアVLM・小型専門モデル・モデル無しのいずれで処理するか事前に選んでコストを抑える
- 抽出結果が正解と一致するかで報酬が検証可能な性質を利用し、表・グラフ・手書きなど汎用モデルが弱い領域にドキュメントVLMをRLでポスト学習させる
- デジタルPDFはファイル内にすでにあるテキスト・メタデータをPDFiumから直接取り出し、画面キャプチャをVLMに投げるより視覚トークンを50〜90%削減する
- 自前ベンチマークParseBenchを公開し、失敗事例からモデル・ハーネス更新までを数日で回す評価ループを内部に持つ

## 使いどころ

- 抽出した値の出典セル位置まで正確なグラウンディングが必要なエージェント型ドキュメント処理
- 大量ページを低コストで処理しつつ精度も譲れないエンタープライズ文書処理基盤
- フロンティアモデル単体でのOCR精度・コストに限界を感じているプロダクトチーム
