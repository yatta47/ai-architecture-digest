---
type: announcement
title: 'Managed Deep Agents v0.9: 自己スケジュール・実行ごとの設定'
title_original: 'Managed Deep Agents v0.9: schedules, per-run configuration, and Slack reactions'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- Managed Deep Agents
- Slack
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/managed-deep-agents-schedules-per-run-configuration-slack
published_at: '2026-10-07'
---

## 概要

エージェントが会話中に自らリマインドや定期タスクを作れるSchedules SDK、実行ごとにモデル・スキル・ツールを切り替える設定、Slackリアクションに対応した。

## 設計のポイント

- スケジュールは依頼者の権限で実行し、結果を同じチャンネルへ返す。
- 1つのデプロイで実行ごとに構成を切り替える。

## 使いどころ

- Slack上の社内エージェントを同僚のように使いたい場面に効く。
