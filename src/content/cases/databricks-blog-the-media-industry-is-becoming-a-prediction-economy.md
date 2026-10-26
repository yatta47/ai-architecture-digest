---
type: opinion
title: メディア・広告で予測経済に備える統合データ・AI基盤という主張
title_original: The media industry is becoming a prediction economy
company: Databricks
industry: media
cloud: []
patterns:
- ai-agent
- generative-recommendation
- data-federation
components:
- Databricks CustomerLake
- Genie
- Lakebase
- Unity Gateway
outcome:
  type: revenue
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/media-industry-becoming-prediction-economy
published_at: '2026-10-26'
---

## 概要

メディア・広告は注目の計測から、成果の予測と証明へ移りつつあるという主張の記事。エージェントと計測は分断されたデータの上では機能せず、統合されガバナンスされたデータとAI基盤が前提になると述べ、PetSmartのロイヤルティデータ活用による成果を例に挙げる。

## 設計のポイント

- 顧客データを別のCDPへ複製せず、ガバナンスされたデータ基盤の上でCustomer 360とオーディエンス活性化を行う。
- 文脈、統制、コスト、選択の4点を基盤の要件として整理する。
- クリーンルームやファーストパーティデータ、クローズドループ計測で成果と施策を結び付ける。

## 使いどころ

- 広告・マーケティング部門で施策とデータ基盤の投資方針を検討する責任者。
- リテールメディアやCTVで成果計測を整えたい事業者。
