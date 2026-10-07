---
type: guidance
title: Databricks AppsのOBO認可：ユーザー権限を引き継ぐ権限対応アプリ
title_original: 'Now GA: Building permission-aware Databricks Apps with on-behalf-of-user authorization'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- guardrails
- ai-agent
components:
- Databricks Apps
- Unity Catalog
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/now-ga-building-permission-aware-databricks-apps-behalf-user-authorization
published_at: '2026-10-07'
---

## 概要

Databricks AppsでGAとなったon-behalf-of-user認可は、ログインユーザーの身元でAPIを呼び、Unity Catalogの行フィルタや列マスクをそのまま適用する。アプリ所有の処理はサービスプリンシパルで行い、両者を処理ごとに使い分ける。

## 設計のポイント

- 操作ごとに「誰の権限で実行するか」を決め、アプリ認可とユーザー認可を併用する
- APIスコープでアプリができる操作を、Unity Catalogの権限で触れるデータを制限する
- 転送されたトークンはリクエスト中のみ使い、欠落時は失敗側に倒し、保存しない

## 使いどころ

- 社内データを扱うAIアシスタントで、利用者ごとのアクセス制御を守りたい場面
- ガバナンスルールをアプリ側で再実装したくない場面
