---
type: opinion
title: LlamaParseに学ぶ、文書に応じて読み方を変えるエージェント型OCR
title_original: 'OCR is dead, long live agentic OCR: lessons from building LlamaParse'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- eval
components:
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/ocr-is-dead-long-live-agentic-ocr
published_at: '2026-10-05'
---

## 概要

従来のOCRは1回の変換で済ませるため、表の崩れなどが長尾の文書で見逃される。LlamaParseの経験から、読み方を文書に適応させ、修正には証拠と検証を求め、実行に明確な上限と目的を置くエージェント型OCRを提案する。

## 設計のポイント

- 表やチャートなど難所にだけ追加処理を割り当て、文書自体が処理を決める。
- 自己修正には証拠を要求し、見た目だけ整って内容が不忠実になる修正を却下する。
- LLMのツール呼び出しループに、実行の上限と目的を設けてUXを担保する。

## 使いどころ

- 複雑な表を含む文書をAIエージェントに読ませるRAG・自動化の担当者。
- 単発変換のパーサーで長尾の失敗に悩むチーム。
