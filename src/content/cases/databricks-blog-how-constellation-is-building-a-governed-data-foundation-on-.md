---
type: case
title: Constellationのガバナンス済みエンタープライズデータ基盤
title_original: How Constellation is building a governed data foundation on Databricks
company: Constellation
industry: other
cloud: []
patterns:
- rag
- guardrails
components:
- Databricks
- Unity Catalog
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-constellation-building-governed-data-foundation-databricks
published_at: '2026-11-12'
---

## 概要

米国最大の原子力事業者Constellationは、ドメイン横断で共通のデータ定義を持つために、Unity Catalogでリネージ、アクセス制御、業務コンテキストを管理するEDPをDatabricks上に構築している。この上で原子力エンジニアリング、停止計画、営業向けのAI活用を進める。

## 設計のポイント

- AI準備で難しいのはモデル選定よりデータの意味の合意とし、共通定義を先に整える。
- Unity Catalogでリネージとアクセス制御を一元化する。
- 共通基盤の上に分野別のAIユースケースを載せる。

## 使いどころ

- ドメイン横断の問いに答えるためデータ定義を統一したい企業。
- 安全性が重視される業界でAI向けデータ基盤を作る組織。
