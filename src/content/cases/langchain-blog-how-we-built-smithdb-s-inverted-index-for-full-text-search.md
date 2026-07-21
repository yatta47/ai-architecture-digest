---
type: case
title: LangSmithのトレース検索基盤:SmithDBにおける転置インデックスの構築・圧縮・クエリ最適化
title_original: 'Full Text Search in SmithDB: Constructing and Querying our Inverted Index (Pt. 2)'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- full-text-search
- llmops
components:
- SmithDB
- DataFusion
- Vortex
- Apache Arrow (arrow-json)
- Tantivy
- Hashbrown
- ahash
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/full-text-search-in-smithdb-constructing-and-querying-our-inverted-index-pt-2
published_at: '2026-06-25'
---

## 概要

LangChainは、エージェント実行トレースを保存するSmithDBにおいて、オブジェクトストレージ上の転置インデックスをどう構築・圧縮・クエリするかを解説している。JSONトレースをタペ形式でフラット化し、文字列インターニングと基数ソートでインデックス構築を約2.2倍高速化した上で、行グループ・整列チャンク・中間タームスピルの3段階フラッシュ閾値によりメモリとGETサイズを制御している。クエリ時にはDataFusionとVortexのLayoutReaderにインデックス有無を組み込み、オブジェクトストレージへのリクエスト前にインデックス参照・カラムスキャン・ショートサーキットを振り分けている。

## 設計のポイント

- Apache Arrowのarrow-json(simdjsonのタープ形式着想)を用いたタペ型パーサーで、ネストしたJSONをアロケーション無しで(path, leaf_value)のフラットなペア列へ変換する。
- 文字列インターニングで各タームを整数IDへ事前変換し、比較コストを出現回数ではなく異なりターム数にスケールさせることで、素朴なソートに比べ構築時間を約2.2倍削減する。
- 行グループ(32MB/50万ターム/64MB)・整列チャンク(~2MB)・中間タームスピル(8MB)という3段階のフラッシュ閾値で、書き込み時のメモリ使用量とワーストケースのGETサイズを両方とも予測可能にし、圧縮時のマージ出力にも同じ閾値を再利用する。
- 圧縮(コンパクション)時はミンヒープによるストリーミングマージを用い、各入力のデコード済みチャンクを1つだけ保持することで、メモリ使用量をインデックス全体のサイズではなくマージ対象の入力数にスケールさせる。

## 使いどころ

- LLM/エージェントの実行トレースのような半構造化JSONログを、書き込み直後から低レイテンシで全文検索したいシステム。
- オブジェクトストレージ上のインデックスセグメントを継続的に圧縮・マージする必要があり、インデックス全体のサイズに関わらずメモリ使用量を一定範囲に抑えたい基盤。
- 1クエリの中でインデックス済み列と未索引列が混在し、述語ごとにインデックス参照/フォールバックスキャンを事前判定してオブジェクトストレージへの無駄なGETを減らしたいクエリエンジン。
- フラッシュ/チャンク閾値を調整することで、メモリとネットワークGETサイズのワーストケースをコスト・レイテンシ要件に合わせてチューニングしたいチーム。
