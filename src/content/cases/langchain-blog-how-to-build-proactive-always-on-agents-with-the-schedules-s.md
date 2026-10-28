---
type: opinion
title: cronで動かす常時稼働型・先回りエージェントの設計
title_original: Why aren't you building proactive agents yet?
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- event-driven
- memory-consolidation
components:
- Managed Deep Agents
- LangSmith
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/proactive-agents
published_at: '2026-10-28'
---

## 概要

先回りして動くエージェントの多くは、cronによる定期実行という単純な仕組みで成り立っているという考察である。記憶の整理(dreaming)、能動的な提案、ノイズのトリアージなどをcronが可能にし、LangSmithのManaged Deepagent実行の7割超が定期実行だという。

## 設計のポイント

- 会話を圧縮して長期記憶を更新するdreamingを、日次cronなどの背景ジョブとして実装する。
- エージェントに目標を持たせ、一定周期で行動を探索させ、その結果を能動的なメッセージとして出す。
- 監視対象のノイズをエージェントがトリアージする。

## 使いどころ

- ユーザーの指示を待たず動く個人アシスタントや専門エージェントを作りたいチーム。
- 定期的な情報収集や監視を自動化したい場面。
