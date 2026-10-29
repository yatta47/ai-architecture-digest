---
type: announcement
title: 'Managed Deep Agents v0.10: ブラウザ操作と非同期サブエージェント'
title_original: 'Managed Deep Agents v0.10: Browser use and asynchronous subagents'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- human-in-the-loop
components:
- Managed Deep Agents
- LangSmith
- Slack
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/managed-deep-agents-browser-use-and-asynchronous-subagents
published_at: '2026-10-29'
---

## 概要

Managed Deep Agents v0.10は、APIの無いサイトを操作するブラウザ機能と、長時間タスクをバックグラウンドで走らせる非同期サブエージェントを追加した。Slackスレッドへの返信先保持や停止ボタンも加わった。

## 設計のポイント

- ブラウザは専用サンドボックスで動かし、アクセシビリティツリー基準のツールでコンテキスト消費を抑える。
- ログイン時はbrowser_handoffで人に操作を渡し、パスワードをモデルやトレースに残さない。
- 長い処理は非同期サブエージェントに任せ、メインのエージェントは対話を続けて結果を会話に戻せる。

## 使いどころ

- APIが無いWebサービス上の予約や手続きをエージェントに任せたい場面。
- コーディングエージェントが変更後のUIを自分で動作確認する場面。
