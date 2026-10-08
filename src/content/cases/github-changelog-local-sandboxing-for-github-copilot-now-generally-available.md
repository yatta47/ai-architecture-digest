---
type: announcement
title: Copilotエージェントをローカルでサンドボックス実行
title_original: Local sandboxing for GitHub Copilot now generally available
company: GitHub
industry: cross-industry
cloud: []
patterns:
- defense-in-depth
- policy-as-code
- guardrails
components:
- GitHub Copilot CLI
- Microsoft Execution Containers
- VS Code
- MCP
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-07-local-sandboxing-for-github-copilot-now-generally-available
published_at: '2026-10-07'
---

## 概要

Copilot CLI・アプリ・VS Codeでローカルサンドボックスが一般提供。MXCが共通ポリシーをWindows・macOS・Linuxのネイティブ制御へ変換し、ファイル、ネットワーク、認証情報へのアクセスを制限する。

## 設計のポイント

- 共通ポリシーをOSごとの制御に変換して提供する。
- ローカルMCPなどツール類にも同じ制限をかける。

## 使いどころ

- エージェントに端末操作を任せつつ被害範囲を限定したい場面に効く。
