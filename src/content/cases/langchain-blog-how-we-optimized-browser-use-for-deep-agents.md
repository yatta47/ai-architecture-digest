---
type: case
title: Deep Agents向けブラウザ操作ツールの最適化
title_original: How We Optimized Browser Use for Deep Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- eval
components:
- Stagehand
- Browserbase
- LangSmith
- Managed Deep Agents
- Playwright MCP
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-we-optimized-browser-use-for-deep-agents
published_at: '2026-11-03'
---

## 概要

LangChainはManaged Deep Agentsにブラウザ操作を載せるため7つのツールセットを比較し、Stagehandを選んで、LangSmithのトレースで無駄を見つけて改善し、評価で検証した。長い連続呼び出しと大きなページ内容というコンテキスト課題へのツール設計が焦点。

## 設計のポイント

- トレースで非効率を特定し、ツールを直して評価で効果を確認する反復を回す。
- ページ内容を絞り、1回の返却量を抑える。
- ホスト型ブラウザでCAPTCHAや大量並列を任せる。

## 使いどころ

- APIの無いサイトを操作するエージェントを作るとき。
- Webアプリのエンドツーエンド検証。
