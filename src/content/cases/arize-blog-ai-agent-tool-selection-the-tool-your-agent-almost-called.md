---
type: case
title: 決定モデルでツール選択を行い、確信度で自己選択へ切り替えるエージェント
title_original: 'AI agent tool selection: The tool your agent almost called'
company: Arize
industry: retail
cloud:
- multi-cloud
patterns:
- ai-agent
- eval
- guardrails
- llmops
components:
- Arize Phoenix
- OpenAI Decisions API
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/ai-agent-tool-selection-decision-tracing/
published_at: '2026-10-19'
---

## 概要

ショッピングエージェントのツール選択を決定モデルに任せ、各選択肢の確率をPhoenixのDECISIONスパンに記録した。確信度0.7未満の選択は誤りが3回に1回と多かったため、その場合は決定モデルを無視してチャットモデルが自分で選ぶようにし、空または未完了の応答を300ターンで21件から3件に減らした。

## 設計のポイント

- ツール選択を決定モデルに、引数の生成をチャットモデルに分担させる。
- 各選択肢の確率と確信度をスパンとして記録し、評価結果を付けてフィルタできるようにする。
- 確信度の閾値は自前の評価で決め、下回ったらチャットモデルへフォールバックする。
- 閾値は100件のテストメッセージに基づく値で、各エージェントで求め直す必要がある。

## 使いどころ

- ツールを多数持つエージェントの選択ミスを減らしたい場面。
- ツール選択の根拠をトレースで可視化したいチーム。
- フォールバック閾値を評価データから決めたい場面。
