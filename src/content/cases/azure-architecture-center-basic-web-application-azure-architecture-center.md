---
type: guidance
title: 学習用途のシンプルなAzure App Service Webアプリ構成（本番非対応）
title_original: Basic web application
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/web-apps/app-service/architectures/basic-web-app
published_at: '2026-05-27'
---

## 概要

Azure App Serviceで単一リージョンのWebアプリケーションを動かす学習・PoC向けの基本アーキテクチャ。App ServiceのEasy AuthでMicrosoft Entra ID認証を行い、SQL Databaseに接続し、Application Insightsで監視する構成だが、可用性ゾーンやプライベートネットワークなど本番向け機能は省略されている。
