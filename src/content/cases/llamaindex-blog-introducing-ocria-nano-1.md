---
type: announcement
title: CPUで動く8.1Mパラメータの軽量文書パーサOCRia-nano-1
title_original: Introducing OCRia-nano-1
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- inference-optimization
components:
- OCRia-nano-1
- LiteParse
- OCRia-1
- Hugging Face
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-ocria-nano-1
published_at: '2026-11-23'
---

## 概要

LlamaIndexが8.1Mパラメータの文書解析モデルOCRia-nano-1をオープンウェイトで公開した。OCR・表構造・レイアウト復元をCPU上のLiteParseで実行し、1ページ平均426msでTesseractの2倍以上の速度を示す。難しい文書は大型VLMのOCRia-1に振り分ける使い分けを提案している。

## 設計のポイント

- 軽量モデルを文書処理の第一段として使い、難文書のみ大型VLMへ回す階層構成にする。
- PDF内の既存テキスト層を優先し、欠落時のみOCRを適用して処理量を抑える。
- 大型モデルからの蒸留で教師データを作り、小型モデルの精度を確保する。

## 使いどころ

- 大量ドキュメントの取り込みパイプラインをCPUのみで低コストに回したい場合。
- エージェントがアップロードされたファイルを素早く読む場面。
- 請求書や契約書など標準的な文書の一次パース。
