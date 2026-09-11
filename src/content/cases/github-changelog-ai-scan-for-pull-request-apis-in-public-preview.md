---
type: announcement
title: プルリクエスト向けAIスキャンをAPIで組織横断に管理
title_original: AI Scan for pull request APIs in public preview
industry: cross-industry
cloud: []
patterns:
- ai-security-scanning
components:
- GitHub Advanced Security
- AI Scan
- CodeQL
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-10-ai-scan-for-pull-request-apis-in-public-preview
published_at: '2026-09-10'
---

## 概要

GitHub Advanced Securityの「AI Scan for pull requests」機能を、組織/リポジトリ単位のREST APIで有効化・無効化できるようになった。UIで個別設定する代わりに、複数リポジトリへプログラム的にAI駆動のセキュリティ検出をロールアウトできる。

## 設計のポイント

- 組織レベルの無効化設定がリポジトリレベルの設定より優先される階層構造にする
- UI操作ではなくAPIでロールアウトできるようにし、多数リポジトリへの一括適用を可能にする

## 使いどころ

- 多数のリポジトリにAI駆動のPRセキュリティ検出を段階的に展開したいセキュリティ管理者
