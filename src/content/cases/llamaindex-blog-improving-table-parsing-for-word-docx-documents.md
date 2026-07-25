---
type: case
title: Word XMLの表要素をページ位置に対応付けてLlamaParseの.docx表抽出精度を改善
title_original: Improving Table Parsing for Word (.docx) Documents
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/improving-table-parsing-for-word-docx-documents
published_at: '2026-07-19'
---

## 概要

PDFと違い.docxはXMLとして表構造(セル・結合・書式)を明示的に保持しているが、ページ境界情報を持たないためページ単位の出力に使えていなかった。LlamaIndexは独自技術でWord XMLの表要素を実際のレンダリング後のページ位置へ対応付けることで、結合セルやネストした表、リッチな書式を持つ表の抽出精度を大きく改善した。

## 設計のポイント

- .docxをPDFに変換してからVLMでパースする『素直な』方法は、XMLが持つ構造情報を捨てて難しい問題にわざわざ変換してしまうと判断し、XML由来の構造を直接活かす方式を選んだ
- Word XMLには結合セル(gridSpan/vMerge)が明示的な属性として存在するため、空間推論に頼らずそのまま構造を保持できる
- XMLにはページ境界情報がないという制約に対し、レンダリング結果とXML構造を対応付ける独自技術でページ位置を解決した

## 使いどころ

- 複雑な結合セルやネスト表を含むWord文書を扱う文書処理パイプライン
- 契約書や報告書などWordで作成された表データをMarkdown/構造化データとして取り込みたいエージェント
