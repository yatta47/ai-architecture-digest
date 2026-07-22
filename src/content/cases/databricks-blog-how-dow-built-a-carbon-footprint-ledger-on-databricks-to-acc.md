---
type: case
title: Databricksで構築するカーボンフットプリント台帳:製品別CO2e算定と低炭素証明書発行の自動化
title_original: How Dow Built a Carbon Footprint Ledger on Databricks to Accelerate Sustainability at Scale
company: Dow
industry: manufacturing
cloud: []
patterns:
- mlops
- data-federation
- decision-execution
components:
- Databricks
- Apache Spark
- Delta Lake
- Unity Catalog
- MLflow
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-dow-built-carbon-footprint-ledger-databricks-accelerate-sustainability-scale
published_at: '2026-07-21'
---

## 概要

Dowは全社に散在する調達・製造・輸送・排出量データをDatabricks上に統合し、Carbon Footprint Ledger(CFL)としてISO14067・GHG Protocol Product Standardに準拠した製品別カーボンフットプリント(PCF)を算定する仕組みを構築した。Apache Spark・Delta Lake・Unity CatalogによるデータパイプラインとMLflowベースのMLOpsによる最適化モデルにより、従来数週間かかっていた全製品分のPCF計算を大幅に高速化し、監査可能な低炭素製品証明書の発行を実現した。これによりDowのDecarbia製品ポートフォリオを支え、顧客のScope3排出量削減にも寄与している。

## 設計のポイント

- Delta Lakeでパイプライン各段階をACIDトランザクション・タイムトラベル可能なテーブルとして永続化し、監査可能な系譜(lineage)を確保する
- Unity Catalogによるガバナンス層で、機微な製造データや排出係数へのアクセスをきめ細かく制御する
- MLflowを用いたMLOpsで最適化モデルをバージョニング・監視付きの本番サービスとして運用し、パラメータ更新を即座にパイプラインへ反映する
- Apache Sparkの分散処理により複数業務ドメインのデータ結合・変換をスケールさせ、算定時間を数週間から大幅に短縮する

## 使いどころ

- EUのCSRDなど規制対応のため、製品単位の温室効果ガス排出量を監査可能な形で開示する必要がある製造業
- 顧客からのScope3排出量削減要求に応え、低炭素製品の証明書発行や残高管理を行いたい企業
- サイロ化した複数部門・地域のデータを統合し、大規模な最適化計算を本番運用したいエンタープライズデータ基盤チーム
