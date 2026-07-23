---
type: guidance
title: Responses APIの組み込みFile SearchツールでベクトルストアRAGを実装
title_original: File search
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- Responses API
- File Search
- Vector Stores
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/tools-file-search
published_at: '2025-07-22'
---

## 概要

OpenAIのResponses APIにはFile Searchというホスト型ツールがあり、ファイルをアップロードしたベクトルストアに対してモデルがセマンティック検索・キーワード検索を自動実行できる。開発者は検索基盤を自前実装せずに、ファイルアップロードとベクトルストア作成のみでRAGを組み込める。

## 設計のポイント

- ホスト型ツールのためリトリーバル処理のコードを自前で書く必要がなく、モデルが必要と判断した時点で自動的にツール呼び出しを行う。
- ベクトルストアへのファイル登録後はステータスがcompletedになるまで確認してから検索対象に含める。
- file_searchツールをtools配列に追加しvector_store_idsを指定するだけでResponses API呼び出しに組み込める。

## 使いどころ

- 自前でベクトルDBや検索パイプラインを構築せずに社内文書QAを立ち上げたい場合。
- 複数ファイルにまたがる知識ベースを素早くプロトタイピングしたいチーム。
