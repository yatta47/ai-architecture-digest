---
type: announcement
title: Parse Gatewayがページ単位の複雑度推定で文書解析パーサーを自動ルーティング
title_original: Parser routing is all you need
industry: cross-industry
cloud: []
patterns:
- document-processing
- multi-model-routing
- cost-optimization
components:
- LlamaParse
- LiteParse
- Parse Gateway
- MCP
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/parser-routing-is-all-you-need
published_at: '2026-07-30'
---

## 概要

LlamaIndexは、文書全体を一律に高精度パーサーまたは高速パーサーで処理するのではなく、LiteParseのis_complex機能でページ単位に複雑度を推定し、理由と深刻度に応じてLiteParseまたは複数のLlamaParse階層へルーティングするParse Gatewayを発表した。同じロジックをMCPサーバー経由でエージェントからも呼び出せる。

## 設計のポイント

- ファイル単位でなくページ単位で複雑度を推定し、必要なページだけ高コストな解析階層に回す
- テキスト欠落・スキャン画像・埋め込み画像・文字化け・ベクター文字など複雑度の理由ごとに基準となる処理階層を割り当てる
- 理由が3つ以上重なる場合や、レイアウトの複雑さが単独で高い場合は階層をエスカレーションする
- Web UIとMCPサーバーで同一の複雑度推定アルゴリズムを共有し判断の一貫性を保つ

## 使いどころ

- スキャン文書と通常のテキストPDFが混在する大量文書パイプラインを扱うチーム
- コスト・レイテンシ・精度のトレードオフをページ単位で最適化したいドキュメント処理基盤
- エージェントが解析要否を自律判断してから最適なパーサーを呼び分けたいRAG構築者
