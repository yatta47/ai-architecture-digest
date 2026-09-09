---
type: case
title: データベースブランチを土台にしたマルチエージェントTDD開発フレームワーク「Consort」
title_original: 'Introducing Consort: Test-driven development on a branching database'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- ci-cd
- spec-driven-development
- human-in-the-loop
components:
- Lakebase Postgres
- Consort
- VS Code
- Alembic
- Flyway
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/introducing-consort-test-driven-development-branching-database
published_at: '2026-09-09'
---

## 概要

OSSのエージェント開発フレームワークConsortは、Lakebase Postgresのコピーオンライトのデータベースブランチをテストの『本物のデータ』として使い、モックへの依存をなくす。プロダクトオーナーやDBA、アーキテクトレビュアーなど役割ごとのエージェントが、決定的なステートマシンである『コンダクター』に導かれてred/green/refactorサイクルを回す。

## 設計のポイント

- データベースをコードと同様にブランチ可能にし、破壊的なテストも他メンバーに影響を与えず実行後に破棄する
- スキーマ変更をバージョン管理されたマイグレーションとしてコードと一体でPRに含め、DBAがコードオーナーとしてレビューできるようにする
- コードを書く役割（driver）がテストを書き換えて通すことを禁止し、実データベース上でのグリーンのみを成功と認める
- 各エージェントには全コードではなくスコープを絞ったコンテキストパッケージ（対象テストや設計要件のみ）を与えてドリフトを防ぐ
- オーケストレーション役はエージェントではなく決定的なステートマシンとし、人間承認ゲートを確実に機能させる

## 使いどころ

- AIエージェントにコード生成させつつテストの信頼性を担保したい開発チーム
- モックのドリフトに悩まされてきた統合テストを実データベースへ置き換えたい場合
- スキーマ変更を本番相当の環境で事前検証してから昇格させたいデータベース運用
