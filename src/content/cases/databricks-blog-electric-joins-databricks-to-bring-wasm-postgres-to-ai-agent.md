---
type: announcement
title: DatabricksがElectricを迎え入れ、エージェントサンドボックス向けWASM PostgresとLakebase同期を統合
title_original: Electric Joins Databricks to Bring WASM Postgres to AI Agent Sandboxes
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- memory-consolidation
- data-federation
components:
- Electric
- PGlite
- Lakebase
- Postgres
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/electric-joins-databricks-bring-wasm-postgres-ai-agent-sandboxes
published_at: '2026-08-11'
---

## 概要

エージェントは実行時に必要なデータを都度判断し、サンドボックス化された環境で動作し、複数エージェントがグループで協調するという点で従来のアプリケーションと異なり、単一の管理されたPostgresだけでは要件を満たせない。DatabricksはPGlite(サンドボックス内で動くWASM版の軽量Postgres)とリアルタイム同期エンジンを持つElectricを迎え入れ、各エージェントがローカルに低遅延なPostgresを持ちながら、中央のLakebase Postgresと同期して一貫した共有コンテキストを維持できるようにする。

## 設計のポイント

- エージェントの高頻度なローカル状態更新は同一プロセス内の軽量DB(PGlite)で処理し、確定した結果だけを中央の永続ストアに同期する
- 分散するエージェント群のローカル状態と中央のLakebase Postgresをリアルタイム同期エンジンでつなぎ、二重作業や古い状態への作用を防ぐ
- エッジとクラウドの両方をPostgresという単一の標準で統一し、開発者が別々のデータベース技術を学ぶコストを下げる

## 使いどころ

- 複数のエージェントがサンドボックス環境で並行して協調作業を行うシステム
- ネットワーク越しの中央DBアクセスだけでは間に合わない、エージェントのインナーループの高頻度なコンテキスト更新
- エッジで生成された状態を安価なオブジェクトストレージ上の中央DBに集約・ガバナンスしたい場合
