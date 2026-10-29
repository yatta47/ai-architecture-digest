---
type: guidance
title: Managed Deep Agentsでのブラウザ利用の設計と仕組み
title_original: Browser Use in Managed Deep Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- human-in-the-loop
components:
- Managed Deep Agents
- LangSmith
- Open SWE
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/browser-use-in-managed-deep-agents
published_at: '2026-10-29'
---

## 概要

Managed Deep Agentsがエージェントにブラウザを提供する仕組みを解説する。スレット単位とユーザー単位のセッションスコープ、コンテキスト効率の良いツール群、人へのハンドオフによるログイン処理を扱う。

## 設計のポイント

- scopeをthreadとuserで選び、ログイン状態を会話間で共有するか隔離するかを決める。
- ブラウザツールはコンテキスト効率を重視して調整されている。
- 認証情報は人へのハンドオフで扱い、セッションをまたいで永続化できる。

## 使いどころ

- APIで代替できない作業を自動化するエージェントを作るチーム。
- PRのフロントエンド変更をエージェントがE2Eで確認したい開発現場。
