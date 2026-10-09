---
type: guidance
title: Managed Deep AgentsのSlack絵文字リアクションで作る待機表示
title_original: Build great out-of-the-box user experiences with Managed Deep Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llm-gateway
components:
- Managed Deep Agents
- LangSmith LLM Gateway
- Jev
- Slack
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/slack-sdk-managed-deep-agents
published_at: '2026-10-09'
---

## 概要

LangChainのManaged Deep Agents v0.9で、Slackチャネルへのリアクションを関数やデシジョンモデルで動的に選べるAPIが追加された。長時間タスクで受領と解釈を伝えるローディング表示を、軽量な判定で実装する方法を示す。

## 設計のポイント

- リアクションは固定文字列か呼び出し可能オブジェクトで指定でき、ルールベースからモデル判定まで差し替えられる。
- 選択肢を定義した小型デシジョンモデルに分類させ、信頼度が低いときは汎用の絵文字に落とす。
- 同じ絵文字でもエージェントの役割で意味が変わるため、状況の説明で語彙を定義する。

## 使いどころ

- 長時間動くエージェントのユーザー体験を設計するチーム。
- Slackを窓口にした社内エージェントを非開発者に提供する担当者。
