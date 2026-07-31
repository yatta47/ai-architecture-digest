---
type: case
title: 連邦給付プログラムの不正をルール・機械学習・生成AIの多層検知とクロスエージェンシー共有で防ぐ
title_original: Bringing real-time fraud prevention to government benefits
industry: public-sector
cloud: []
patterns:
- data-federation
- event-driven
- human-in-the-loop
components:
- Databricks
- OpenSharing
- Clean Rooms
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/bringing-real-time-fraud-prevention-government-benefits
published_at: '2026-07-29'
---

## 概要

米連邦政府の給付プログラムでは年間2330億〜5210億ドル規模の不正・過払いが発生していると推計される。Databricksは銀行・保険会社向けに培った不正検知の知見をもとに、ルールエンジン・機械学習・生成AIを重ねた多層検知を給付支給前のリアルタイム判定に適用し、OpenSharingとClean Roomsで生データを共有せずに機関横断の不正シグナルを突き合わせる仕組みを構築している。

## 設計のポイント

- ルールエンジン→機械学習→生成AIという段階的にコストと精度が上がる多層検知を単一プラットフォーム上で連携させる
- OpenSharingとClean Roomsで生データをコピー・露出させずに機関横断でエンティティ解決や不正シグナルを突き合わせる
- 検知結果を統計処理で終わらせず、支給保留や不正者リスト追加、証拠パッケージ生成まで一気通貫でつなげる
- 自動化した判定でも最終的な確定は人間がループ内で確認する仕組みを残す

## 使いどころ

- 支給の迅速さと不正検知の両立が求められる社会保障・医療・失業給付などの行政プログラム
- 複数機関にまたがって同一の不正主体を捕捉したい行政のリスク管理部門
- 生データを共有せず横断分析したい機微データを扱う複数組織連携
