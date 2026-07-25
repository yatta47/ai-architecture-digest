---
type: guidance
title: grepかRAGか、エージェントのための検索戦略の使い分け
title_original: Is Grep All You Need? Lexical vs Semantic Search for Agents
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
- document-processing
- full-text-search
components:
- LlamaParse MCP
- LiteParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/is-grep-all-you-need-lexical-vs-sematic-search-for-agents
published_at: '2026-07-18'
---

## 概要

grepのような字句検索はコード検索文脈では有力だが、PDFやOffice文書などの非構造化データをそのまま検索できず、コーパスが数百万件規模になると信号対雑音比とレイテンシが破綻する。LlamaParse MCPやLiteParseで非構造化文書をテキスト化した上で、規模に応じてgrepとハイブリッドRAG（ベクトル＋BM25＋メタデータ）を使い分けるべきだと論じる。

## 設計のポイント

- コーパスが数千件規模でテキストベースならgrep/lexical検索を優先し、シンプルさとレイテンシを取る
- 非構造化文書（PDF・画像・Office）はレイアウト認識パーサーで先にテキスト化してからgrepやRAGに載せる
- コーパスが数百万件規模になったらANNベクトルインデックス＋BM25のハイブリッド検索で線形劣化を回避する

## 使いどころ

- エージェント向け検索基盤の設計時にgrepとRAGのどちらを採用すべきか判断したいチーム
- PDFやOffice文書を含むエンタープライズ全文検索の設計
