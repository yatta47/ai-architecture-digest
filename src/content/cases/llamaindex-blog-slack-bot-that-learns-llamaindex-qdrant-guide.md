---
type: guidance
title: 会話を学習して答えるSlackボットを構築しRenderへ展開する
title_original: Building a Slack Bot that Learns with LlamaIndex, Qdrant and Render
industry: cross-industry
cloud: []
patterns:
- rag
- event-driven
components:
- Slack
- LlamaIndex
- Qdrant
- Render
- Flask
- Slack Bolt
- ngrok
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-a-slack-bot-that-learns-with-llamaindex-qdrant-and-render-c88d4aa72840
published_at: '2024-01-25'
---

## 概要

Slackのメッセージイベントを受けて会話内容を蓄積し、ワークスペースの出来事への質問に答えるボットを作ってRenderに本番展開するチュートリアル。

## 設計のポイント

- メッセージのイベント購読を取り込み口にして知識を逐次追加する。
- ボットはメンションされたときだけ返信させる。

## 使いどころ

- 社内チャットの知識を検索・回答に使いたいチーム。
