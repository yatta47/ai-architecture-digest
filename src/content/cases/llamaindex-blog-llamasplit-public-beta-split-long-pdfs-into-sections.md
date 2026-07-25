---
type: announcement
title: 複数文書が混在するPDFをAIでカテゴリ別に自動分割するLlamaSplit
title_original: Split Documents into Clear, Targeted Sections with LlamaSplit
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LlamaSplit
- LlamaParse
- LlamaExtract
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/split-document-into-clear-targeted-sections-with-llamasplit
published_at: '2026-07-19'
---

## 概要

LlamaSplitは、履歴書の束や混在した金融文書など1つのファイルに複数の文書が束ねられているケースで、ページ内容をAIで分類し同一カテゴリの連続ページをまとめてセグメント化するベータAPIである。ページ範囲と信頼度スコード付きでセグメントを返し、各セグメントをLlamaExtract等の下流処理にルーティングできる。

## 設計のポイント

- ページ単位でユーザー定義カテゴリに分類し、同一カテゴリの連続ページをグルーピングしてセグメント化する
- 自然言語のカテゴリ説明を与えるだけでよく、事前のスキーマ定義や学習が不要
- 文書全体を分類するLlamaParse Classifyとは異なり、1ファイル内の複数文書間の境界検出に特化させている
- 分割結果をLlamaExtractでの個別抽出やエージェントワークフローへのルーティングと組み合わせられる

## 使いどころ

- 採用イベントで集まった大量の履歴書PDFを個別の候補者ドキュメントに分割したい人事部門
- 請求書・領収書・契約書が混在した金融文書バンドルを種類ごとに仕分けたい金融機関
- 訴訟書類のパッケージを訴状・証拠・宣誓供述書に分けて個別分析したい法務部門
