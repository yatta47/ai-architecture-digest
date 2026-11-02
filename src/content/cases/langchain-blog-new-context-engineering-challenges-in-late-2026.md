---
type: opinion
title: 常時稼働・能動型エージェントがもたらす新たなコンテキストエンジニアリング課題
title_original: New context engineering challenges in late 2026
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- Deep Agents
- LangChain
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/context-engineering-challenges-late-2026
published_at: '2026-11-02'
---

## 概要

LLMがループでツールを呼びサンドボックスで動くエージェント構成が定着し、要約やツール結果のオフロード、サブエージェントなどの定番手法も出揃ったと整理する。一方で、バックグラウンドで常時動く能動的な目標指向エージェントでは通知の出し方など新たな課題があると論じる。

## 設計のポイント

- 起動はイベントフィードやハートビートで行い、ユーザーへのプッシュは多すぎず少なすぎない水準に調整する必要がある。
- 要約、ツール結果のオフロード、スキルによる段階的開示、ツール検索、サブエージェントによる分離が現在の標準的な手法である。

## 使いどころ

- 長時間・常時稼働するエージェントを設計するチームが課題を事前に把握したい場合。
- 既存のコンテキスト管理手法の到達点を整理したい場合。
