---
type: opinion
title: メモリとUXで作るプロアクティブエージェントの知見
title_original: What We've Learned Building Proactive Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- event-driven
- memory-consolidation
- human-in-the-loop
components:
- LangChain
- Managed Deep Agents
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/what-weve-learned-building-proactive-agents
published_at: '2026-11-17'
---

## 概要

プロアクティブエージェントは、実世界のイベントやスケジュールを契機にバックグラウンドで目標に向けて動く。社内のGTM AgentとRobinの運用経験から、ユーザーの注意を無駄にしないための鍵はメモリとUXだと整理している。

## 設計のポイント

- 起動契機をイベント、開発者設定のスケジュール、エージェント自身のスケジュールの3種で設計する。
- 確認や承認の依頼は注意コストなので、必要な時だけ人に戻す設計にする。
- 定期的なメモリ更新ジョブで学習内容を蓄積する。

## 使いどころ

- バックグラウンドで動く営業・開発エージェントを設計するチーム。
- 人への確認頻度を調整したいエージェント運用者。
