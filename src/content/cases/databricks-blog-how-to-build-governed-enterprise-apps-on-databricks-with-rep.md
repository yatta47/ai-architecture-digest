---
type: guidance
title: Replit AgentとDatabricks Appsでガバナンス済みの業務アプリを作る
title_original: How to build governed enterprise apps on Databricks with Replit and Lakebase
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- policy-as-code
components:
- Replit Agent
- Databricks Apps
- Lakebase
- Unity Catalog
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-build-governed-enterprise-apps-databricks-replit-and-lakebase
published_at: '2026-10-08'
---

## 概要

Replit Agentで平易な指示から業務アプリを作り、Databricks AppsとLakebase Postgresにデプロイする手順を紹介する。認証やUnity Catalogの権限が自動で継承され、承認工程を減らせる。

## 設計のポイント

- アプリをDatabricks Appsとして配備し、認証とアクセス制御を継承させる。
- Lakebaseを自動プロビジョニングして取引データ用DBの構築を省く。

## 使いどころ

- 業務部門が自分でデータアプリを作りたいが、セキュリティ審査を短縮したい場面に効く。
