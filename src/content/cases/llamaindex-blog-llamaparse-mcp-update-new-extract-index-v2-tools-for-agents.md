---
type: announcement
title: LlamaParse MCPへのExtract・Index v2ツール追加とプロダクト別サーバー分割
title_original: Extending the LlamaParse MCP for More Document Processing Power
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- document-processing
- ai-agent
components:
- LlamaParse MCP
- Index v2
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/extending-the-llamaparse-mcp-for-more-document-processing-power
published_at: '2026-07-18'
---

## 概要

LlamaParse MCPにExtractサービスとIndex v2の連携が追加され、エージェントがJSONスキーマ生成から構造化抽出、ファイルシステム的なインデックス操作までを行えるようになった。同時にMCPサーバーが肥大化した反省から、parse/classify/extract/split/indexごとのプロダクト特化サーバーへ再編し、並列実行と文脈の絞り込みを両立させた。

## 設計のポイント

- 抽出前にgenerateExtractionConfigでJSONスキーマとルールを明示的に定義し、抽出結果のばらつきを抑える
- Index v2をベクトル検索専用にせず、listIndexes/findFilesInIndex/readFileFromIndex/grepFileFromIndexなどファイル操作的なツール群として提供する
- 単一の巨大MCPサーバーではなく設定ID単位のプロダクト特化サーバーに分割し、エージェントが並列にツール呼び出しできるようにする

## 使いどころ

- フォルダ内の文書を分類してから種類ごとに異なる抽出設定を適用する自律的なドキュメント処理エージェント
- PDFや画像を含む非構造化データをエージェントのナレッジ層として活用したいプロジェクト
