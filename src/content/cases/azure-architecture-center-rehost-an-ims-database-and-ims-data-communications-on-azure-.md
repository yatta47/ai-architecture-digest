---
type: guidance
title: Raincode IMSqlを使ったIMSメインフレームのAzureリホスト構成
title_original: Rehost an IMS database and IMS data communications on Azure by using Raincode IMSql
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/rehost-ims-raincode-imsql
published_at: '2026-06-26'
---

## 概要

本記事は、IMSデータベースとIMSデータコミュニケーション（DC）を持つメインフレームワークロードを、Raincode IMSqlを用いてAzureへリホストする参照アーキテクチャを解説する。既存のCOBOLアプリケーションやJCLバッチジョブを書き換えることなく、SQL Server Service Brokerによる通信の仲介やSQL Managed Instance上での階層データモデルの再現、DL/I呼び出しのSQLクエリへの変換により機能的等価性を保ったまま移行できる。Virtual Machine Scale SetsやAzure Logic Apps、ExpressRouteなどを組み合わせてオンプレミス端末からのアクセスを維持しつつ、Azure PaaSの可用性・災害復旧機能を活用する構成になっている。
