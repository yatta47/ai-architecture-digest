---
type: guidance
title: 書き込み先行ログ(WAL)を正とするオブジェクトストレージ基盤でPostgresをエージェント時代向けに再設計する
title_original: 'Object storage + WAL: Lakebase Postgres for the agentic era'
company: Databricks
industry: cross-industry
cloud:
- aws
patterns:
- unified-transactional-analytical-storage
- memory-consolidation
- disaster-recovery
components:
- Amazon S3
- Lakebase Postgres
- WAL
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/object-storage-wal-lakebase-postgres-agentic-era
published_at: '2026-08-27'
---

## 概要

Lakebase PostgresはPostgresのWAL(書き込み先行ログ)をデータベースの正とみなし、データファイルをそこから派生するキャッシュとして扱うことで、コンピュートとストレージを分離した。safekeeperがWALのクォーラム複製でコミットを確定し、pageserverが非同期にページを具体化してオブジェクトストレージへ不変履歴として蓄積することで、エージェントが必要とする本番コピーの分離作成や巻き戻しを安価なポインタ操作にしている。

## 設計のポイント

- WALをソース・オブ・トゥルースとし、データファイルは派生・キャッシュ可能な表現として扱う
- コミットはsafekeeperのクォーラム確認のみで完了させ、ページの具体化はトランザクションのクリティカルパスから外して非同期に行う
- オブジェクトストレージには可変ファイルシステムではなく追記専用の不変履歴として保存し、DBの”コピー”をファイル複製ではなくポインタにする
- 読み出しはRAM→ローカルNVMe→オブジェクトストレージの順で、ページIDとLSNを指定するGetPage@LSNで一意に解決する

## 使いどころ

- エージェントが本番データの分離コピーを都度作って試行錯誤する必要があるワークロード
- 大量の一時ブランチを安価に作って短時間で破棄したいCI的な使い方
- 特定時点への巻き戻しやロールバックを頻繁に必要とするデータベース運用
