---
type: case
title: HPがCustomerLakeでAI対応CDPを構築し施策準備を2時間に短縮
title_original: How HP is building an AI-ready CDP with Databricks CustomerLake
company: HP
industry: other
cloud:
- multi-cloud
patterns:
- ai-agent
- business-intelligence-resilience
components:
- Databricks CustomerLake
- Genie
- Marketing Lakehouse
- Unity Catalog
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/hp-ai-ready-cdp-databricks-customerlake
published_at: '2026-10-20'
---

## 概要

HPは既存のDatabricks基盤上にCustomerLakeでCDP機能を統合し、ガバナンス済みモデルと属性を公開した。オーディエンス準備は2〜3カ月から2時間に、CDPのTCOは最大40%減、インテントデータは75から約2万トピックへ拡大した。

## 設計のポイント

- CDPを別製品に切り出さず、顧客データのあるガバナンス済みプラットフォームに埋め込む。
- GenieとCustomerLakeで信頼できる文脈をマーケターの日常の判断に提供する。
- メディア・ブランド・インテントなど外部シグナルを統合し、データ共有の期間を短縮する。

## 使いどころ

- コンポーザブルCDPの運用コストと遅延に悩むマーケティング部門。
- 自社データ基盤上で施策用データを素早く整備したい企業。
