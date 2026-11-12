---
type: announcement
title: Slack上で権限を引き継ぐ統制付きデータAI「Genie」の一般提供
title_original: Genie in Slack is now generally available
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- text-to-sql
- guardrails
components:
- Databricks Genie
- Unity Catalog
- Slack
- MCP
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/genie-slack-now-generally-available-governed-ai-cowork-right-where-work-happens
published_at: '2026-11-12'
---

## 概要

DatabricksのGenieアプリがSlackで一般提供となり、DMやチャンネルのメンションで根拠付きの回答を得られる。質問者の権限でUnity Catalogの制御が適用され、承認後にMCPコネクタで文書やチケットを更新し、スケジュール分析も実行できる。

## 設計のポイント

- 質問者自身の権限で実行し、DMでもチャンネルでもガバナンスを保つ。
- 回答に出典を付け、確認できるようにする。
- 更新系の操作は承認を挟んでMCP経由で実行する。

## 使いどころ

- 会話の場で指標を確認したい事業部門。
- データ権限を保ったままAIを社内に展開したい企業。
- 質問から調査・更新まで一貫させたいチーム。
