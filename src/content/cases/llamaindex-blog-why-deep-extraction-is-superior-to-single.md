---
type: guidance
title: 単発抽出の限界を超えるディープエクストラクション:検証ループ付きエージェント抽出
title_original: Why Deep Extraction Is Superior to Single-Pass Extraction
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- eval
components: []
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/deep-extraction
published_at: '2026-07-18'
---

## 概要

単発抽出パイプラインは行の欠落や不整合を検知する仕組みを持たず、200ページの請求書などで途中から静かに失敗することがある。ディープエクストラクションは、部分ごとにサブエージェントが抽出し合計値などとの整合性を検証、不一致があれば再抽出するループを回すことで、フィールド精度を10-20%から99-100%まで引き上げる。

## 設計のポイント

- 文書を構成要素(明細行・ヘッダー・合計・埋め込み表)ごとにサブエージェントへ分割して抽出する
- 抽出結果を文書内の合計値などと突き合わせる検証エージェントを挟み、不一致なら再抽出する
- VLMを用いて表やチャート・画像など非テキスト要素もデータとして読み取れるようにする
- 検証基準の厳格さを下流ワークフローのリスクの高さに合わせて調整する

## 使いどころ

- 50明細行を超える請求書や証券会社の取引明細など高リスク文書の処理
- 合計値の突合など下流のコンプライアンス検証が必須な金融・保険業務
