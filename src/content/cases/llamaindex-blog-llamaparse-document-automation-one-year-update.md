---
type: announcement
title: LlamaParse/LlamaCloud 1周年、ドキュメント自動化基盤の歩み
title_original: 'LlamaCloud One Year Later: The Complete Document Automation Platform'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- rag
components:
- LlamaParse
- LlamaExtract
- LlamaIndex Workflows
outcome:
  type: revenue
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamacloud-one-year-later-the-complete-document-automation-platform
published_at: '2026-07-19'
---

## 概要

LlamaIndex CEOによるLlamaParseパブリックベータ提供開始から1年の振り返り。レイアウト・表・グラフを理解する高精度パースと抽出・インデックス化・分類をビルディングブロックとして提供し、セルフサーブ収益は700%超成長、Cemex・Rakuten・Carlyleなどが企業ナレッジ基盤上でリサーチコパイロットや請求書処理を自動化している事例を紹介する。

## 設計のポイント

- 標準OCRでは崩れる表・レイアウト・グラフを理解する『レイアウト認識』パースでAIエージェントが信頼できる文脈を提供する
- パース・抽出・インデックス化・分類を独立したビルディングブロックとして提供し、用途に応じて組み合わせられるようにする
- 文書処理層(LlamaParse)とワークフロー実行層(LlamaIndex Workflows)を分離し、リサーチ用途と業務自動化用途の両方をカバーする

## 使いどころ

- 社内データルーム全体を横断検索するエンタープライズのリサーチコパイロット構築
- 人の目視確認を残しつつ請求書処理やExcel変換などの業務プロセスを自動化したい企業
