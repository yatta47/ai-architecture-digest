---
type: opinion
title: 文書パースの正解を定義するDocument Parsing Protocol
title_original: Introducing the Document Parsing Protocol
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
- rag
components:
- Document Parsing Protocol
- ParseBench
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-the-document-parsing-protocol
published_at: '2026-10-28'
---

## 概要

LlamaIndexは、文書パースの正しい出力を定める作業草案DPP 0.1を公開した。パーサーごとに表の見出しの扱いが異なるとエージェントの回答が誤るため、140のルールと例で基準を示す。

## 設計のポイント

- 複数行見出しを平坦化せず各段を保持し、スパンを表現できるHTML tableで出力する。
- パーサー独自のラベルを生成せず、紙面に印字された内容を保つ。
- ParseBenchの注釈ルールを基準としてまとめ、準拠性を評価できるようにする。

## 使いどころ

- エージェントやRAGの入力となる文書パースの品質を比較したい開発者。
- 表や図を含む文書の抽出精度が回答品質を左右する業務。
