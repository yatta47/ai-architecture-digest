---
type: guidance
title: API ManagementでSPAのアクセストークンをブラウザに残さず保護する構成
title_original: Use API Management to Protect Access Tokens in Single-Page Applications
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/web-apps/guides/security/secure-single-page-application-authorization
published_at: '2026-07-02'
---

## 概要

JavaScriptのシングルページアプリケーションでアクセストークンをブラウザのセッションやローカルストレージに保存せず、XSS攻撃から保護するためのステートレスなアーキテクチャを解説する。Azure API ManagementがBackends for Frontendsパターンとして機能し、Microsoft Entra IDからOAuth2アクセストークンを取得してAESで暗号化したうえでHttpOnly Cookieに格納し、以降のAPI呼び出しをプロキシしてAuthorizationヘッダーを自動付与する。MSAL.jsなどのトークン管理ライブラリをフロントエンドに組み込む必要がなくなる点が特徴。
