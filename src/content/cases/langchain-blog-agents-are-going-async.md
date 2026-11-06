---
type: guidance
title: 非同期サブエージェントで応答性と生産性を両立するエージェント設計
title_original: Agents are going async
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- parallel-execution
components:
- LangChain
- Deep Agents
- Claude Code
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/agents-are-going-async
published_at: '2026-11-05'
---

## 概要

長時間タスクがReActループをブロックする問題に対し、ユーザーと対話するオーケストレーターとバックグラウンドで動く非同期サブエージェントに分ける設計を、Deep Agentsの機能として紹介する。開始・確認・更新・キャンセル・一覧の5ツールで管理する。

## 設計のポイント

- サブエージェントを即時復帰で起動し、オーケストレーターがユーザー対応を続けられるようにする。
- 5つの管理ツールで、進捗確認、追加指示、キャンセルを制御する。
- update_strategyで、実行中タスクへの追加指示を割り込み再起動にするかなどを切り替える。

## 使いどころ

- 長いコーディングや調査をバックグラウンドで進めつつ対話を維持したいエージェント。
- 複数の大きなタスクを並行して処理したい場面。
