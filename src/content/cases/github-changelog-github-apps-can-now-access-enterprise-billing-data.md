---
type: announcement
title: GitHub Appsにエンタープライズ課金データへのアクセス権限を追加
title_original: GitHub Apps can now access enterprise billing data
ai_relevant: false
company: GitHub
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-26-github-apps-can-now-access-enterprise-billing-data
published_at: '2026-08-26'
---

## 概要

GitHub Appsに新たに「enterprise billing」権限が追加され、読み取り専用または読み書き権限を選択してエンタープライズの課金APIにアクセスできるようになった。従来は個人のPersonal Access Tokenに依存していたため、担当者の異動や退職で課金自動化が止まるリスクがあったが、アプリのインストールトークンで完結できるようになりこの問題を解消する。あわせてPATより高いレート制限も得られる。
