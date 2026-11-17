---
type: announcement
title: VS CodeのCopilotローカルハーネス廃止とCopilotハーネスへの移行
title_original: VS Code retires the Local harness in February 2027
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
components:
- VS Code
- GitHub Copilot
- Copilot SDK
outcome:
  type: reliability
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-16-vs-code-retires-the-local-harness-in-february-2027
published_at: '2026-11-16'
---

## 概要

VS Code 1.146でローカルハーネスが非推奨となり、2027年2月に削除される。後継のCopilotハーネスはCopilot SDK上で動き、権限支援やサンドボックス制限を管理者が強制できる。

## 設計のポイント

- エージェントの実行基盤をCLIやアプリと共通化し、セッションを継続できるようにする。
- 管理者が実行時権限とサンドボックスを強制できる。

## 使いどころ

- VS CodeでCopilotエージェントを使う開発組織。
