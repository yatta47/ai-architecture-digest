---
type: announcement
title: 'Databricks AI Runtime一般提供: ガバナンス下のサーバーレスGPU学習'
title_original: AI Runtime is generally available
company: Databricks
industry: cross-industry
cloud: []
patterns:
- llmops
- fine-tuning
- gpu-fleet-reliability
components:
- Databricks AI Runtime
- Unity Catalog
- Ray
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/ai-runtime-generally-available
published_at: '2026-10-21'
---

## 概要

AI RuntimeがGAとなり、マネージドGPUをDatabricks内で提供する。秒単位の起動、学習前後のGPU・ネットワーク健全性チェック、Unity Catalogによる統制を備える。数百社が利用中という。

## 設計のポイント

- 起動遅延を抑えるRDMA対応GPUと環境キャッシュで実験を高速化する。
- 学習中のGPU・ネットワーク健全性チェックで大規模学習の信頼性を高める。
- Unity Catalogの境界内で学習データを保護・監査可能にする。

## 使いどころ

- コーディングエージェントが多数の学習実験を回す環境。
- 機微データを扱うGPU学習を分離せず実施したい場面。
