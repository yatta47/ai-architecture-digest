---
type: case
title: 毎分40億メトリクスを捌く社内観測基盤Argusを単一リージョン依存からマルチジオ構成へ
title_original: How Salesforce Eliminated Single-Region Risk and Reduced Downtime Blast Radius at 4B Metrics/Min
ai_relevant: false
company: Salesforce
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-salesforce-eliminated-single-region-risk-and-reduced-downtime-blast-radius-at-4b-metrics-min/
published_at: '2026-08-05'
---

## 概要

Salesforceの社内観測基盤Argusは毎分約40億メトリクスを取り込む規模に成長する一方、単一AWSリージョン依存がリージョン障害時に可視性を全社的に失わせるリスクを抱えていた。3チーム・6か月がかりの再設計で、メトリクスを発生源に近い地域で処理・保存する『geo-local』モデルへ移行し、フェデレーションクエリ層でリージョンをまたぐ問い合わせを集約することで、コストを抑えながら障害の影響範囲を局所化した。
