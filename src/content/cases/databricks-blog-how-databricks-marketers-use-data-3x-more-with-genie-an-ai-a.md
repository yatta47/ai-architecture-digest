---
type: case
title: 会話型分析アシスタント「Marge」でマーケターのデータ活用頻度を3倍にした社内展開
title_original: How Databricks marketers use data 3x more with Genie, an AI analytics assistant
company: Databricks
industry: cross-industry
cloud: []
patterns:
- text-to-sql
- context-engineering
components:
- Genie Agents
- Genie One
- Unity Catalog
- Marketing Lakehouse
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/databricks-marketers-use-data-3x-genie-ai-analytics-assistant
published_at: '2026-09-15'
---

## 概要

Databricksは自社マーケティング部門向けに、ガバナンスされたMarketing Lakehouse上でGenie Agentsを使った会話型分析アシスタント「Marge」を構築。自然言語の質問に数秒でガバナンスされた回答を返し、マーケターがデータを意思決定に使う頻度が3倍、組織の85%超が利用、アナリティクス人員を増やさずにインサイトへのアクセスを拡大した。

## 設計のポイント

- メタデータ・テーブル説明・リネージをUnity Catalogに集約し、Genieに新人アナリスト相当のビジネスコンテキストを与える
- よくある高価値な質問には検証済みロジックと例クエリを事前に登録し回答の信頼性を担保する
- 組織固有の用語(パイプライン/リージョン/会計年度など)の解釈をGenieに明示的に教え込みあいまいさを減らす

## 使いどころ

- 複数システムに散らばるデータとダッシュボードの乱立で「どの数字を信じればいいか」わからないマーケティング組織
- アナリティクスチームの人員を増やさずにセルフサービス分析への需要増に対応したい企業
