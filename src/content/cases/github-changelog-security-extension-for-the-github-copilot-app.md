---
type: announcement
title: Copilotアプリ内でコードスキャン指摘を説明・修正するセキュリティ拡張
title_original: Security extension for the GitHub Copilot app
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- guardrails
components:
- GitHub Copilot app
- GitHub code scanning
- Copilot CLI
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-28-security-extension-for-the-github-copilot-app
published_at: '2026-10-28'
---

## 概要

GitHubセキュリティ拡張(公開プレビュー)により、Copilotアプリ内でコードスキャンのアラートを重大度順に確認し、CopilotにExplain/Fixを依頼できる。修正はローカル作業コピーに限られ、/security-reviewで未コミット変更もレビューできる。

## 設計のポイント

- Copilotの修正はローカルに留め、commit/pushは人が確認してから行う。
- アラート閲覧・却下はAIを使わず、Explain/Fix/レビューのみAIクレジットを消費させる。
- 管理者がポリシーと管理設定でプラグインのインストールを制御できる。

## 使いどころ

- コードスキャン指摘の対応に時間がかかっている開発チーム。
- PR前に変更をAIで事前セキュリティレビューしたい場面。
