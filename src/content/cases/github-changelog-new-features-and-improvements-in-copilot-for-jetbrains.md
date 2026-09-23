---
type: announcement
title: 'Copilot for JetBrains 1.18.0: 補助承認・共有スキル・MCPツール制御'
title_original: New features and improvements in Copilot for JetBrains
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- context-engineering
components:
- GitHub Copilot
- JetBrains IDE
- Codex agent
- GitHub MCP Server
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-22-new-features-and-improvements-in-copilot-for-jetbrains
published_at: '2026-09-23'
---

## 概要

Copilot for JetBrains 1.18.0は、低リスクのツール呼び出しを自動承認する補助承認、過去メッセージの再編集と巻き戻し、組織共有のスキル・指示、Codexエージェントのプランモード、MCPツールの永続的な個別制御を追加した。

## 設計のポイント

- 低リスクは自動承認し高リスクのみ人に確認するリスク階層型の承認で、中断を減らしつつ判断権を残している。
- 再編集時に会話とファイル変更の両方を巻き戻し、途中からやり直せるようにしている。
- 組織・エンタープライズのスキルと指示を共有して、エージェント運用のばらつきを抑えている。

## 使いどころ

- エージェントの承認ダイアログの多さに悩む開発者。
- 組織標準のスキルや指示を配布したい管理者。
- MCPツールの利用範囲を細かく制限したいチーム。
