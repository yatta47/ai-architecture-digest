---
type: announcement
title: 'Genie One: 回答を行動に変えるデスクトップアプリ・文書コラボ・エージェント化機能'
title_original: 'Beyond answers: New Genie One features to turn insights into action'
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- text-to-sql
- context-engineering
components:
- Genie One
- Genie Agents
- Databricks Apps
- Unity AI Gateway
- Databricks SQL
- Genie Ontology
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/beyond-answers-new-genie-one-features-turn-insights-action
published_at: '2026-08-28'
---

## 概要

DatabricksのAIアシスタントGenie Oneに、ブラウザを離れてアクセスできるデスクトップアプリ、会話をそのまま編集・コメント可能な共有ドキュメントに変換する機能、ドメイン知識を蓄えた会話を再利用可能なGenie Agentとして保存する機能などが追加された。あわせて、ダッシュボードやSQLクエリから自動抽出したビジネスルールをGenie Ontologyスニペットとして取り込み、ファイルアップロードやMCP経由の書き込みアクションも可能にし、Unity AI Gatewayのガバナンス配下で企業データへのアクセス範囲を広げている。

## 設計のポイント

- 1回限りの質問応答で終わらせず、会話をGenie Agentとして保存・再利用可能にすることで、同じ文脈調査を繰り返さずにチームで共有できるようにする
- Metric Views/Domains/Pagesなどのモデル化されたビジネス文脈に加え、ダッシュボードやクエリから自動抽出したontologyスニペットを組み合わせ、権限を尊重したまま関連文脈を検索できるようにする
- MCP経由の書き込みアクション(チケットコメント・ドキュメント作成・メール送信)をUnity AI Gatewayでガバナンス下に置き、単なる質問応答から実行(アクション)まで拡張する

## 使いどころ

- データに関する洞察を毎回ゼロから調査・整形せず、レポートやエージェントとして再利用したいデータチーム
- 既存のエンタープライズガバナンス・権限モデルを維持したまま、AIアシスタントに書き込み系のアクションまで任せたい組織
