---
type: guidance
title: Deep Agentsにおけるコンテキストロット対策の5手法
title_original: 'Context Engineering: How Deep Agents Remember'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- context-engineering
- memory-consolidation
- ai-agent
components:
- Deep Agents
- LangChain
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/context-engineering-deep-agents-remember
published_at: '2026-10-14'
---

## 概要

長時間動くエージェントのコンテキスト肥大による精度低下(context rot)に対し、Deep Agentsがツール結果のオフロード、要約、スキルの遅延ロード、サブエージェント分離、長期メモリの5手法をミドルウェアで適用する様子を解説する。メモリはプレーンファイルで保持され、モデルを替えても引き継げる。

## 設計のポイント

- 大きなツール結果はファイルに退避しプレビューのみをモデルに見せる
- ノイズの多い作業はサブエージェントの別コンテキストで行い、結果だけ返す
- 学習内容をユーザー管理のファイルに保存し、モデル非依存にする

## 使いどころ

- 長期タスクを回すエージェントの設計者
- 競合調査など繰り返し実行するエージェントに記憶を持たせたいチーム
