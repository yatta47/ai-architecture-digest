---
type: opinion
title: 音声エージェントは顧客コンテキストで価値が決まる
title_original: Voice agents are here. Context turns them into real customer value
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- voice-agent
- context-engineering
components:
- Databricks
- DIVA blueprint
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/voice-agents-are-here-context-turns-them-real-customer-value
published_at: '2026-10-28'
---

## 概要

音声エージェントは、通話相手の文脈を持って初めて価値を生むと主張する。Databricks上でガバナンス済みデータの隣にエージェントを置き、オントロジーで回答を根拠づけ、通話ごとの学習ループを回す構成を紹介する。

## 設計のポイント

- 通話相手の文脈とオントロジーで回答を根拠づけ、決まった規則の範囲内で応答する。
- 約200ミリ秒という人間の応答間隔に追従できる高速な判断で各ターンを調整する。
- まず量の多い定型通話を1つ選んで効果を測り、DIVAブループリントで次へ広げる。

## 使いどころ

- 配送の予約変更やドライブスルー注文など、定型の音声対応が多い業務。
- 顧客データを活用した音声エージェントを導入したい企業。
