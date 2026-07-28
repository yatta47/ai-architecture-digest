---
type: case
title: 公共部門文書の大規模パーシングによる商機発掘プラットフォーム
title_original: Pursuit Transforms Public Sector Insights with LlamaParse
company: Pursuit
industry: public-sector
cloud: []
patterns:
- document-processing
- full-text-search
components:
- LlamaParse
outcome:
  type: revenue
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/pursuit-transforms-public-sector-insights-with-llamaparse
published_at: '2026-07-24'
---

## 概要

公共機関向け営業支援を行うPursuitは、9万以上の自治体・機関にまたがる予算書・戦略計画・議事録などの多様な公共部門文書をLlamaParseでパースし、検索・フィルタリング可能なデータベース化した。1週末で400万ページを処理できる規模のパイプラインを実現し、複雑な文書からの抽出精度も25〜30%向上したことで、クライアントによる商機発掘と受注率向上につながった。

## 設計のポイント

- LlamaParseにより表・図・スキャン画像を含む複雑な文書フォーマットからも高精度にデータを抽出する
- クロール・ダウンロード・保存だけでなく、検索・フィルタリング可能な形へ変換するところまでを一気通貫で設計する
- 1つのスケーラブルな基盤で数百万ページ規模のドキュメント取り込みを短期間で処理できるようにする

## 使いどころ

- 官公庁・自治体向け営業（B2G）のために大量の公開文書から商機を発掘したい企業
- 予算書・議事録など非構造データに埋もれた情報をパラメータで絞り込み検索したい場合
- 多様なフォーマット（PDF・スキャン画像・表）が混在する文書群を横断的に扱いたいケース
