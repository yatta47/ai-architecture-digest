---
type: case
title: Manager/Planner/Programmerの3段階グラフで動く非同期オープンソースコーディングエージェントOpen SWE
title_original: 'Introducing Open SWE: An Open-Source Asynchronous Coding Agent'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- human-in-the-loop
components:
- Open SWE
- LangGraph
- Daytona
- GitHub
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/introducing-open-swe-an-open-source-asynchronous-coding-agent
published_at: '2026-06-16'
---

## 概要

LangChainが、GitHubに直接統合される非同期・クラウドホスト型のオープンソースコーディングエージェントOpen SWEを公開。Manager/Planner/Programmer(Reviewer内包)の3段階LangGraphアーキテクチャで計画・実装・レビューを分離し、各タスクを隔離サンドボックス(Daytona)で実行することで、人間承認なしに任意のシェルコマンドを安全に実行できるようにした。

## 設計のポイント

- Manager→Planner→Programmer(Reviewer内包)の3段階グラフに分割し、計画・実装・レビューの責務を分離する
- 各タスクを隔離されたサンドボックス(Daytona)で実行し、人間承認なしに任意のシェルコマンドを安全に実行可能にする
- 計画段階でHuman-in-the-loopの承認を挟み、実行中もdouble-textingで指示を随時差し込めるようにする

## 使いどころ

- GitHub issueから長時間非同期で複雑なコーディングタスクを任せたいチーム
- 計画とレビューを含む信頼性の高いコーディングエージェントを構築したい場合
