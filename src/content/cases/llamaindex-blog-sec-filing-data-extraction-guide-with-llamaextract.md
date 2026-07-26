---
type: guidance
title: LlamaExtractで100ページ超のSEC 10-K開示資料から構造化データを抽出する
title_original: Mining Financial Data from SEC Filings with LlamaExtract
company: LlamaIndex
industry: financial-services
cloud: []
patterns:
- document-processing
components:
- LlamaExtract
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/mining-financial-data-from-sec-filings-with-llamaextract
published_at: '2026-07-19'
---

## 概要

LlamaIndexは、100ページを超えるSEC 10-K/10-Q開示資料から財務指標やリスク要因を構造化抽出するLlamaExtractの活用法を、Nvidiaの10-Kを例に解説する。Pydanticによるスキーマ設計や、必須/任意フィールドの使い分けなど長文書抽出特有の設計指針を示す。

## 設計のポイント

- Pydanticモデルで申告種別・財務ハイライト・リスク要因などを階層構造のスキーマとして定義し、文書の論理構成をスキーマに反映させる
- 必須フィールドが多すぎるとハルシネーションを誘発し、任意フィールドが多すぎると情報の欠落を招くため、フィールドの必須/任意を戦略的に調整する
- 類似概念が異なる文脈で登場する長文書では、フィールドの説明文に期待する挙動やNG例を具体的に書き込むことで抽出精度を高める
- 抽出結果にページ番号を含めることで、どの箇所から抽出したかを検証できるようにする

## 使いどころ

- SEC提出書類から財務指標を体系的に評価したいアナリストや投資家
- 契約書や研究論文など長文の非構造化文書から構造化データを抽出したいチーム
- リスク要因の開示情報を継続的にモニタリングしたいリスク管理部門
