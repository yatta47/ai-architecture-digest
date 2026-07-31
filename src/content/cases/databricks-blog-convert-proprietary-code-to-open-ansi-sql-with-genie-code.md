---
type: announcement
title: Genie Codeのエージェント型コンバータが独自方言SQLをANSI SQLへ並列変換
title_original: Convert proprietary code to open ANSI SQL with Genie Code
industry: cross-industry
cloud:
- multi-cloud
patterns:
- multi-agent-orchestration
- parallel-execution
components:
- Databricks Genie Code
- Unity Catalog
- Databricks Lakebridge
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/convert-proprietary-code-open-ansi-sql-genie-code
published_at: '2026-07-30'
---

## 概要

Databricksのコーディングエージェント「Genie Code」に、T-SQLやSnowflake、Redshiftなど複数の独自SQL方言をオープンなANSI SQLへ変換するエージェント型コンバータ（Beta）が追加された。ファイルの複雑度評価とリネージ解析で移行計画を立て、並列に起動したサブエージェント群が構文と意味の両方を検証しながら反復変換する。

## 設計のポイント

- 移行対象コードの複雑度スコアとオブジェクト間リネージを先に可視化し着手順序と同時移行範囲を決める
- 1ファイルにつき1サブエージェントを並列起動し、構文だけでなく元のビジネスロジックが保たれているかを検証させる
- 頻出する修正パターンをカスタムスキルとしてルール化し、以降の変換に自動適用して再発防止する

## 使いどころ

- レガシーなデータウェアハウス（T-SQL/Snowflake/Redshift/Oracle/BigQuery/Teradata）からの移行を計画するデータ基盤チーム
- 数千本規模のストアドプロシージャを人手でなく自動変換で移行したい組織
- 移行後も三部名前空間などの命名規約を一貫適用したいプラットフォームチーム
