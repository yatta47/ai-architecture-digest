---
type: opinion
title: MCPはベクトル検索を不要にするか？RAGとフェデレーテッド検索の役割分担
title_original: Does MCP Kill Vector Search?
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- data-federation
- document-processing
components:
- Model Context Protocol
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/does-mcp-kill-vector-search
published_at: '2026-07-19'
---

## 概要

MCPで各SaaSに直接クエリする『フェデレーテッド検索』が普及しても、複数ソース横断の統一ランキングができない・レイテンシがボトルネックになる・各SaaSの検索品質に依存するという課題から、依然として中央集権的なベクトルインデックス層が必要だと論じる。特に非構造化データ（PDF等）はMCP以前にドキュメントインテリジェンス層でのパース・抽出・チャンク化が不可欠と指摘する。

## 設計のポイント

- 構造化データ（Jira・Salesforce等）はMCPでソースに直接問い合わせ、非構造化データ（PDF・スプレッドシート等）は事前にパース・インデックス化するハイブリッド構成を取る
- 複数MCPサーバーを横断する場合、各ソース固有のランキングに依存せず統一的な関連度スコアリング層を挟む
- 非構造化データにはLlamaParseのような文書インテリジェンス層でメタデータフィルタ付きのハイブリッド検索を提供してからMCPツールとして公開する

## 使いどころ

- MCPだけで全社データ横断検索を実現しようとして精度・レイテンシに悩むアーキテクト
- 構造化/非構造化データが混在するエンタープライズ検索基盤を設計する場合
