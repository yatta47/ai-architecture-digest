---
type: announcement
title: Copilotに8サービスのMCPコネクタを追加（パブリックプレビュー）
title_original: Connect Supabase, Box, Calendly, and more to Copilot
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- policy-as-code
components:
- GitHub Copilot
- MCP
- Box
- Buildkite
- Calendly
- ClickUp
- Mixpanel
- Supabase
- Webflow
- Wix
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-18-connect-supabase-box-calendly-and-more-to-copilot
published_at: '2026-11-18'
---

## 概要

GitHubはGitHub検証済みMCPサーバーをコネクタとして提供し、Box・Supabase・Buildkiteなど8サービスを追加した。一度接続すれば各Copilotクライアントで使え、ビルド失敗の調査からコード修正まで同じセッションで行える。

## 設計のポイント

- 検証済みMCPサーバーをコネクタとして提供し、接続操作をクライアント間で共通化する。
- 企業ではプレビュー機能ポリシーとMCP許可リストで管理者が利用範囲を制御する。

## 使いどころ

- CIや分析基盤、DBの情報を見ながらコード修正したい開発者。
- 外部ツール連携を統制しつつ導入したい組織の管理者。
