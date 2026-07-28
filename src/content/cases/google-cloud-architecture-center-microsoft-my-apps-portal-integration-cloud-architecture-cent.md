---
type: guidance
title: Microsoft My AppsポータルからのGoogleサービスへのシームレスSSO統合
title_original: Microsoft My Apps portal integration
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: productivity
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/identity/integrating-google-services-and-apps-with-azure-ad-portal
published_at: '2026-07-24'
---

## 概要

本ドキュメントは、Microsoft My AppsポータルにGoogleサービスやIAP保護アプリケーションへのリンクを追加し、自動サインオンを実現する方法を解説する。サービスプロバイダー起点のサインオンでは既存のMicrosoft Entra IDセッションが認識されず二重ログインを要求される問題を、ドメインヒント付きの特別なURLを用いることで回避し、さらにグループ単位でリンクの可視性とアクセス権を一括制御する方法も示す。
