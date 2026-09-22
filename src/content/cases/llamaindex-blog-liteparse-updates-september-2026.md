---
type: announcement
title: PDF解析ライブラリLiteParseの高速化・精度向上とビジュアルグラウンディング追加
title_original: LiteParse Updates (September 2026)
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- rag
components:
- LiteParse
- PDFium
- LlamaParse
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/liteparse-updates-september-2026
published_at: '2026-09-22'
---

## 概要

LlamaIndexのオープンソースPDF解析ライブラリLiteParseが、フォークしたPDFiumにmimallocを組み込むなどのメモリ割り当て最適化でテキスト抽出を20〜25%高速化した。表抽出精度の改善やページの複雑さを判定するis-complex APIによるルーティング、マークダウン要素をバウンディングボックス付きで取得できるビジュアルグラウンディングも追加された。

## 設計のポイント

- フォークしたPDFiumにmimallocを組み込みFPDF_LoadPage等のホットパスの細かいメモリ確保・解放オーバーヘッドを削減した
- is-complex APIでスキャン文書や複雑なレイアウトを高速（約3.5ms/ページ）に判定しより高度なパーサーへのルーティングに使える
- マークダウン要素をバウンディングボックス付きのブロックとして出力し抽出結果を元ページの位置に紐付けられるようにした
- 罫線の扱いや段組検出、多言語文書の左右文字方向処理を改善しベンチマーク複数種で精度を検証している

## 使いどころ

- RAGパイプラインで大量のPDFを高速にMarkdown化したいがコストの高い大規模パーサーは使いたくない場合
- 文書の複雑さに応じて軽量パーサーと高度なパーサーを自動的に使い分けたいドキュメント取り込み基盤
- 抽出結果を元のページ位置に遡って検証したい（ビジュアルグラウンディングが必要な）用途
