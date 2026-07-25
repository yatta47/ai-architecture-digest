---
type: guidance
title: ドキュメントAIにおける「パース」と「抽出」の使い分け
title_original: 'Parse vs. Extract: Understanding Two Fundamental Approaches to Document AI'
industry: cross-industry
cloud: []
patterns:
- document-processing
- rag
- context-engineering
components:
- LlamaParse
- LlamaExtract
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/parse-vs-extract
published_at: '2026-07-19'
---

## 概要

ドキュメントAIにおける「パース（構造とコンテキストを保った変換）」と「抽出（定義済みスキーマへの狙い撃ちしたデータ取得）」の違いを整理し、それぞれをいつ使うべきか、また抽出が内部的にパースを前提としていることを解説するガイド記事。RAG・検索・Q&Aにはパース、データベース投入や業務自動化には抽出が適するとしている。

## 設計のポイント

- パースは文書全体の構造・文脈を保持し、検索/RAG/Q&Aのための下地を作る
- 抽出は必ず内部でパースを経たうえで、スキーマ検証とマッピングという追加レイヤーを載せたものとして設計する
- オープンエンドな探索型アプリはパースのみ、フォーム処理など定型業務は抽出のみで足りるケースを見極める
- 本格的なシステムはパースで文脈を確保しつつ抽出で下流システムに接続する両輪構成にする

## 使いどころ

- 自然言語で大量の契約書・判例を横断検索したい法務リサーチシステム
- 請求書や保険金請求など定型フォームから構造化データをシステムに投入したい業務自動化
- 抽出フィールドに応じてワークフローを分岐させたい人事・審査業務
