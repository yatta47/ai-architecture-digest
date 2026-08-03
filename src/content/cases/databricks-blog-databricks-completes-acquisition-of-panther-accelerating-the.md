---
type: announcement
title: DatabricksがPantherを完全買収しエージェント型SOCのセキュリティレイクハウスを構築
title_original: Databricks Completes Acquisition of Panther, Accelerating the Security Lakehouse Era
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- root-cause-analysis
- ci-cd
- data-federation
components:
- Lakewatch
- Panther
- Unity Catalog
- Delta
- OCSF
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/databricks-completes-acquisition-panther-accelerating-security-lakehouse-era
published_at: '2026-08-03'
---

## 概要

従来のSIEMはデータ保持コストとカバレッジのトレードオフを強い、アラートの手動トリアージでアナリストを疲弊させていた。DatabricksはPantherを買収し、オープンなセキュリティレイクハウス基盤Lakewatchに、Detections-as-Codeと自律的なAIトリアージエージェント、100以上の連携コネクタを統合することで、ペタバイト規模のテレメトリ保持とリアルタイムの自動対応を両立させる。

## 設計のポイント

- セキュリティ・IT・ビジネスデータをオープンフォーマット（OCSF/Delta/Parquet）で1つのレイクハウスに統合し、SIEM特有のデータサイロを解消する
- 検知ロジックをUIベースのルールではなくコードとして管理し、CI/CDパイプラインでバージョン管理・テスト・デプロイする
- AIエージェントがアラートのエンリッチメントと一次トリアージを担い、アナリストがチケットを開く前に文脈化された情報を用意する

## 使いどころ

- ログ量の増大でSIEMのライセンスコストとカバレッジがトレードオフになっているセキュリティ運用チーム
- 検知ルールをソフトウェアエンジニアリングの規律（レビュー・バージョン管理）で運用したいSOC
- セキュリティデータをHRやアセット台帳などのビジネスデータと突合して文脈を深めたいケース
