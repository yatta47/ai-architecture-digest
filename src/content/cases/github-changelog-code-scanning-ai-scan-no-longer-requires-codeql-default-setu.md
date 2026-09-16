---
type: announcement
title: CodeQLデフォルトセットアップなしでもAI ScanによるPR脆弱性検出を利用可能に
title_original: Code scanning AI Scan no longer requires CodeQL default setup
company: GitHub
industry: cross-industry
cloud: []
patterns:
- guardrails
components:
- GitHub Advanced Security
- AI Scan
- CodeQL
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-16-code-scanning-ai-scan-no-longer-requires-codeql-default-setup
published_at: '2026-09-16'
---

## 概要

GitHubはプルリクエスト向けのAI Scanについて、これまで必須だったCodeQLデフォルトセットアップの設定を不要にし、コードスキャンとAI Scanを有効化しているリポジトリであれば対象範囲を問わず広く実行できるようにした。追加のセットアップ手順は不要で、権限階層のルールは従来通り組織・エンタープライズレベルで適用される。

## 設計のポイント

- 既存のCodeQL設定要件を取り除き、AI Scan自体の有効化のみで適用範囲を広げる
- 組織・リポジトリ・エンタープライズという既存の権限階層をそのまま流用しガバナンスの一貫性を保つ

## 使いどころ

- CodeQLの既定セットアップを組んでいないリポジトリでもAIによる脆弱性検出を適用したいセキュリティチーム
- GitHub Advanced Securityを契約済みで適用範囲を広げたい組織
