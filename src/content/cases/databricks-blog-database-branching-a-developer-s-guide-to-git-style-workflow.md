---
type: guidance
title: AIエージェントの並列実験を支えるデータベースブランチング
title_original: 'Database branching: a developer''s guide to Git-style workflows'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- parallel-execution
- ci-cd
- policy-as-code
components:
- Databricks Lakebase
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/database-branching
published_at: '2026-09-18'
---

## 概要

データベースブランチングはコピーオンライトで、親と変更差分だけを保持する分離環境を作る。開発者、CIのPR単位、AIエージェントに隔離環境を与え、マイグレーションを正とする運用と、親の保護、モックデータ、TTL、アクセス制御を安全運用の条件に挙げる。

## 設計のポイント

- ブランチは親へマージせず、マイグレーションファイルを正としてデプロイで適用する。
- 短命なエージェント用ブランチを大量に作れるため、親を破壊せず実験できる。
- 親ブランチの保護、機密データの制限、自動クリーンアップで安全に運用する。

## 使いどころ

- PR単位で本番相当のデータでCIを回したいチーム。
- エージェントにDB変更を試させたい開発者。
- スキーマ移行の検証に共有環境を使いたくない組織。
