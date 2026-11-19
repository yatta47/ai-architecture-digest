---
type: announcement
title: Copilot CLIのMicrosoft Entraサインイン（プレビュー）
title_original: GitHub Copilot CLI adds Microsoft Entra sign-in as a preview
company: GitHub
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- policy-as-code
components:
- GitHub Copilot CLI
- Microsoft Entra
- GitHub Enterprise Managed Users
- Microsoft 365 Copilot
- Work IQ MCP
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-17-github-copilot-cli-adds-microsoft-entra-sign-in-as-a-preview
published_at: '2026-11-17'
---

## 概要

GitHub Copilot CLIがMicrosoft Entra認証をパブリックプレビューで対応した。EMUアカウントへのサイレントSSOと、Microsoft 365 Copilotライセンス経由のモデル利用の両方が選べる。WindowsとmacOSが対象でLinuxは今後対応予定。

## 設計のポイント

- 認証経路で推論基盤を切り替える（EMUならGitHub推論、M365ならMicrosoft 365推論）。
- モデルの利用上限や課金は組織のライセンス設定側で管理する。
- Work IQ MCPサーバーでMicrosoft 365の業務データをコンテキストに渡せる。

## 使いどころ

- Entra中心のID基盤でCLIエージェントを統制したい企業。
- GitHubアカウント無しでM365ライセンスのモデルをターミナルから使いたい場面。
