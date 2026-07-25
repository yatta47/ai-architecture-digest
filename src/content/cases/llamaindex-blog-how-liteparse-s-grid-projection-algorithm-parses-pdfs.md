---
type: guidance
title: LiteParseのグリッド投影アルゴリズムでPDFの座標情報をテキストに再構成する仕組み
title_original: 'How LiteParse Turns PDFs Into Text: A Deep Dive Into the Grid Projection Algorithm'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LiteParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/how-liteparse-turns-pdfs-into-text-a-deep-dive-into-the-grid-projection-algorithm
published_at: '2026-07-18'
---

## 概要

LlamaIndexのオープンソースPDFパーサーLiteParseは、座標情報しか持たないPDFのテキスト要素を等幅文字グリッドに投影することで、表や複数カラムのレイアウト構造を保ったままテキスト化する。行のグルーピング、アンカー抽出、スナップ分類、フォワードアンカーによる位置制約という段階を経て、テーブル構造の崩壊を防ぐ。

## 設計のポイント

- 全文結合方式(レイアウト崩壊)とフルレイアウト解析(高精度だが低速)の中間として、座標を等幅グリッドに投影する第三の方式を採用した
- X座標をクォーター単位に丸めてアンカー化し、微妙な位置ズレを許容しつつ列の整列を検出する
- 既にスナップされたアイテムの位置を『フォワードアンカー』として後続行に伝播させ、表の列がズレないようにする
- アンカー数が少なく行が横幅いっぱいに広がるブロックは『地の文』と判定し、グリッド投影ではなく単純な空白結合にフォールバックする

## 使いどころ

- 請求書や財務諸表など、表構造を保ったままテキスト化してAIエージェントに読ませたい文書処理パイプライン
- クラウド非依存でPDFを高速・軽量にパースしたい開発者
