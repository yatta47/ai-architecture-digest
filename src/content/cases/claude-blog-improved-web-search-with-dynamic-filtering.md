---
type: announcement
title: 検索結果をコードで事前フィルタし精度とトークン効率を両立するWeb Search
title_original: Increase web search accuracy and efficiency with dynamic filtering
company: Quora
industry: media
cloud: []
patterns:
- context-engineering
components:
- Claude Opus 4.6
- Claude Sonnet 4.6
- web_search tool
- web_fetch tool
- code execution
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/improved-web-search-with-dynamic-filtering
published_at: '2026-02-17'
---

## 概要

Web検索・Web取得ツールにコード実行によるdynamic filteringを追加し、生のHTMLをそのままコンテキストに読み込む代わりに検索結果を事前にコードでフィルタしてから渡せるようにした。BrowseCompとDeepsearchQAのベンチマークで平均11%の精度向上と24%のトークン削減を達成し、Poe by Quoraでの導入事例も紹介する。

## 設計のポイント

- 検索結果の生HTMLをそのまま推論させるのではなく、Claude自身がコードを書いて関連情報だけを抽出しコンテキストに載せる
- 精度とトークンコストはモデルやベンチマークによってトレードオフが異なるため、自社の代表的な検索クエリで事前に評価することを推奨する

## 使いどころ

- 技術文書の横断調査や引用の裏取りなど、多くのWebページを渡り歩いて特定の答えを探す必要があるエージェント
- 複数モデルを横断提供するプラットフォーム事業者が、Web検索精度をフロンティアモデル並みに引き上げたい場合
