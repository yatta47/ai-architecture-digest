---
type: announcement
title: Rust書き換えでどこでも動くようになったLiteParse v2.0
title_original: Up to 100x Fast Parsing with LiteParse v2.0 and Rust
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- document-processing
components:
- LiteParse
- PDFium
- tesseract-rs
- WASM
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/liteparse-v2-0-runs-everywhere
published_at: '2026-07-18'
---

## 概要

LLMを使わずにPDFから構造化テキストを抽出するLiteParseがRustで全面書き換えされ、Node/Python/Rust/WASMのネイティブパッケージとして配布されるようになった。Node起動のオーバーヘッドがなくなったことで小さな文書は5〜100倍、大きな文書でも約3倍高速化し、ブラウザやエッジランタイムでも動作する。

## 設計のポイント

- コアロジックをRustに一本化し、各言語バインディングへの変更伝播とパフォーマンス・安全性を同時に得る
- WASMターゲット向けにシステム依存部分（OCRなど）をコールバック方式にスタブ化し、ブラウザ完結の解析を実現する
- リアルタイムエージェント用途を意識し、大容量文書でも高速な解析速度を維持する

## 使いどころ

- リアルタイム性が求められるエージェントやアプリケーションでのPDF読み込み
- エッジランタイムやブラウザ上で完結させたいプライバシー重視のドキュメント処理
