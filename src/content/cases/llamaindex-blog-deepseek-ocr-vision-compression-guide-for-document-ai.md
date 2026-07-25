---
type: opinion
title: DeepSeek-OCRの視覚圧縮技術とドキュメント解析への示唆
title_original: Beyond OCR
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- multi-agent-orchestration
- context-engineering
- memory-consolidation
components:
- DeepSeek-OCR
- LlamaParse
- SAM
- CLIP
- ColPali
- Qwen2.5-VL
- InternVL3
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/beyond-ocr
published_at: '2026-07-19'
---

## 概要

DeepSeekが発表した DeepSeek-OCR は、テキストを高圧縮率の視覚トークンとして表現し1,000テキストトークンを100視覚トークンまで圧縮しても97%の精度を維持できることを示した。LlamaIndexはこの技術がドキュメントパース（LlamaParseの多エージェント方式）とどう関係し、将来の文書処理・エージェントメモリ設計にどう影響するかを論じている。

## 設計のポイント

- SAM(高解像度知覚)とCLIP(大域的圧縮)の2段構成エンコーダで圧縮率を用途別に切り替え可能にする
- LlamaParseはVision/OCR/Structure/LLM/Synthesisの複数エージェントを協調させ、構造化されたmarkdown/JSON出力を作る
- 『Vision Memory』では直近の文脈は高精細テキストで保持し、古い文脈ほど低解像度の視覚表現に圧縮する人間の記憶に似た設計を取る
- 圧縮率が上がるほど精度上限が下がる（20倍圧縮で約60%）ため、重要文書では構造化パースを残す判断が必要

## 使いどころ

- コンテキストウィンドウのコストを抑えたいRAG・文書Q&Aシステムの設計者
- 財務報告書や法務契約など高精度な構造化パースが必要なエンタープライズ文書処理
- 長い会話履歴を限られたコンテキスト内に保持したいエージェントのメモリ設計
