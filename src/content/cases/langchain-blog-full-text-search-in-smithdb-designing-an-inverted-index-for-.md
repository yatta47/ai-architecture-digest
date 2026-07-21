---
type: case
title: エージェントトレース向け全文検索基盤SmithDBの転置インデックス設計
title_original: 'Full Text Search in SmithDB: Designing an Inverted Index for Object Storage'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- full-text-search
- llmops
components:
- SmithDB
- LangSmith
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/full-text-search-in-smithdb-designing-an-inverted-index-for-object-storage
published_at: '2026-06-11'
---

## 概要

LangChainは可観測性基盤SmithDBにおいて、巨大でネストの深いJSONペイロードを持つエージェントトレースに対し中央値400ミリ秒で全文検索とJSONフィルタリングを実現する転置インデックスをゼロから設計した。ログ向けの既存全文検索エンジンとは異なり、ペイロードが巨大でZipf分布に従う語彙、オブジェクトストレージ特有のレイテンシ・スループット制約に最適化した独自のストレージレイアウトを採用している。json_key（パス存在)、json_key_search（キー付き値)、search（全文)という3種類のクエリ形状を明確に区別して設計している。

## 設計のポイント

- パス存在(json_key)・キー付き値(json_key_search)・全文検索(search)という3種類のクエリ形状を明確に分離し、それぞれに適したインデックス構造を設計する
- 巨大かつZipf分布の語彙を持つペイロードではソース:インデックス比が1:1.9に達するため、インデックスをコンパクトかつプルーニング可能な形で1ファイルに収める
- オブジェクトストレージ上ではリクエスト数×読み取りバイト量がコストを支配するため、ポスティングリストや位置情報リストを不要に取得しないクエリ実行計画を設計する
- 用語(term)・ポスティング(posting)・位置(position)の3要素からなる転置インデックスにより、フレーズ検索や複数トークンのクエリを全ペイロードスキャンなしで処理する

## 使いどころ

- エージェントのトレースログのような巨大でネストの深いJSONペイロードを大量に扱う可観測性プラットフォームの検索基盤設計
- オブジェクトストレージにデータを保持しつつステートレスにスケールしたいシステムで、レイテンシとコストを抑えた検索インデックスを構築したい場合
- ツール出力やエラーメッセージなど自由テキストの中身を高速に横断検索したいLLMアプリケーション運用者
